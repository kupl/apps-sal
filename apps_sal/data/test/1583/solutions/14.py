import math
a,b,x=map(float,input().split())
volume=a**2*b
if volume<x*2:
    sub=volume-x
    sub=sub/a*2/a
    ans=math.degrees(math.atan(sub/a))
else:
    x=x/a*2/b
    ans=90.0-math.degrees((math.atan(x/b)))
print(ans)
