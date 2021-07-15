import math
a,b,x = map(int,input().split())
if x>=a*a*b*0.5:
    theta = math.degrees(math.atan(2*(a*a*b-x)/a**3))
else:
    theta = math.degrees(math.atan(0.5*a*b*b/x))
print(theta)
