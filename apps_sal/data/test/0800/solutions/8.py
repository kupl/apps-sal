import math
from math import atan2 as t
a=[]
for i in range(int(input())):
  x,y=map(int,input().split())
  a.append(180*t(y,x)/math.pi)
a.sort()
ans=a[-1]-a[0]
for i in range(len(a)-1):
  ans=min(ans,360-a[i+1]+a[i])
print(ans)
