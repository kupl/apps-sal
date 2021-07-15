import math
a,b,x = map(int,input().split())
if a*a*b/2 <= x:
    j = 2*(b/a - x/(a**3))
else:
    j = b*b*a/(2*x)
ans = math.degrees(math.atan(j))
print(ans)
