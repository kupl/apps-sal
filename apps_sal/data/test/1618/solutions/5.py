n=int(input())
l=list(map(int,input().split()))
m=int(input())
s=[]
for i in range(m):
	s+=[list(map(int,input().split()))]
h=[]
a=0
for i in range(m):
	b=l[s[i][0]-1]
	t=max(b,a+1)
	h+=[t]
	a=t+s[i][1]-1

for i in h:
	print(i)
