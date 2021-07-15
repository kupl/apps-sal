from collections import Counter
n,a,b=map(int,input().split())
s=Counter();ans=0
for i in range(n):
	x,vx,vy=map(int,input().split())
	tmp=vy-a*vx
	ans+=s[tmp]-s[(vx,vy)]
	s[tmp]+=1;s[(vx,vy)]+=1
print(ans*2)
