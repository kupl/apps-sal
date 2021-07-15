from collections import Counter
from sys import stdin
n,a,b=map(int,stdin.readline().split())
s=Counter();ans=0
for i in range(n):
	x,vx,vy=map(int,stdin.readline().split())
	tmp=vy-a*vx
	ans+=s[tmp]-s[(vx,vy)]
	s[tmp]+=1;s[(vx,vy)]+=1
print(ans*2)
