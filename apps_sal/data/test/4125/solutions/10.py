n,x=map(int,input().split())
xlist= list(map(int,input().split()))
if n == 1:
  print(abs(xlist[0]-x))
  return
ylist = []
for i in range(n):
  ylist.append(abs(xlist[i]-x))
from functools import reduce
from math import gcd
print(reduce(gcd,ylist))
