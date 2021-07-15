'''
Created on 2020/08/16

@author: harurun
'''
N,T=map(int,input().split())
t=list(map(int,input().split()))
ans=T
s=t[0]
for i in range(1,N):
  if t[i]-s>=T:
    ans+=T 
  else:
    ans-=T-(t[i]-s)
    ans+=T
  s=t[i]
print(ans)  
