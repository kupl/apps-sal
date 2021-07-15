import math
a,b,x=list(map(int,input().split()))


def f(a,b,deg):
  theta=math.radians(deg)
  if b*math.tan(math.pi/2-theta)<=a:
    return b*b*math.tan(math.pi/2-theta)*a/2
  else:
    return a*a*b-a*a*math.tan(theta)*a/2


l=0
r=90
while r-l>=10**-6:
  mid=(l+r)/2
  #print(mid,f(a,b,mid))
  if x-10**-6<=f(a,b,mid)<=x+10**-6:
    print(mid)
    return
  if f(a,b,mid)>x:
    l=mid
  else:
    r=mid
print(l)

