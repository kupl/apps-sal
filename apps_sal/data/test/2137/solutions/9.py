from collections import Counter
n,a,b=map(int,input().split())
s,s1=Counter(),Counter();ans=0
for i in range(n):
	x,vx,vy=map(int,input().split())
	tmp=vy-a*vx
	ans+=s[tmp]-s1[(vx,vy)]
	s[tmp]+=1
	s1[(vx,vy)]+=1
print(ans*2)
