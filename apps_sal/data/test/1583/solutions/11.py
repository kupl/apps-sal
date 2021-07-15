from math import pi
from math import atan2

a, b, x = map(float, input().split())
ans = 0
x /= a
if (x > a*b / 2): 
    ans = atan2((a*b-x)*2, a*a) * 180 / pi
else:
    ans = atan2(b*b, x*2) * 180 / pi
print (ans)
