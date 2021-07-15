import math
a, b, x = map(int, input().split())
if a*a*b//2 <= x:
    print(math.degrees(math.atan((a*a*b-x)/a*2/a/a)))
else:
    print(math.degrees(math.atan(b/(x/a*2/b))))
