import collections

s=list(input())
a=[0]

s.reverse()

mod=2019

mod10=1

for i in range(len(s)):
  x=int(s[i])
  y=a[-1]
  ans=(x*mod10+y)%mod
  a.append(ans)
  mod10=(mod10*10)%mod
  
ans1=0

c = collections.Counter(a)
d=list(c.values())

for r in d:
  if r>=2:
    ans1+=(r*(r-1))//2
    
print(ans1)
