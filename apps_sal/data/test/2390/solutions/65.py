import sys
input=sys.stdin.readline
l=[[0,0,0]]
r=[[0,0,0]]
n,c=list(map(int,input().split()))
for i in range(n):
	x,v=list(map(int,input().split()))
	r.append([x,v])
	l.append([c-x,v])
r.sort()
l.sort()
now=0
for i in range(n):
	now+=r[i+1][1]
	r[i+1].append(max(now-r[i+1][0],r[i][2]))
	if r[i+1][2]==r[i][2]:
		r[i+1][0]=r[i][0]
now=0
for i in range(n):
	now+=l[i+1][1]
	l[i+1].append(max(now-l[i+1][0],l[i][2]))
	if l[i+1][2]==l[i][2]:
		l[i+1][0]=l[i][0]
ans=0
for i in range(n+1):
	a=l[i][0]
	b=r[n-i][0]
	ans=max(l[i][2]+r[n-i][2]-min(a,b),ans)
print(ans)

