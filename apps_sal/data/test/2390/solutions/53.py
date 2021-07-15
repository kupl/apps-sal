n,c=map(int,input().split())
xv=[list(map(int,input().split()))for _ in range(n)]
l=[0]
s=0
for x,v in xv:
	s+=v
	l.append(max(l[-1],s-x))
r=[0]
s=0
for x,v in xv[::-1]:
	s+=v
	r.append(max(r[-1],s-(c-x)))
ans=max(l+r)
s=0
for i in range(n):
	s+=xv[i][1]
	ans=max(ans,s-2*xv[i][0]+r[n-i-1])
s=0
for i in range(n-1,-1,-1):
	s+=xv[i][1]
	ans=max(ans,s-2*(c-xv[i][0])+l[i])
print(ans)
