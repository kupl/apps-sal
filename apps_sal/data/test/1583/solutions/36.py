import math
a, b, x = map(int,input().split())

if x > a*a*b / 2:
    print(math.atan(2*(a*a*b - x) / (a*a*a)) * (180 / math.pi))
else:
    print(math.atan(a*b*b/(2*x)) * (180 / math.pi))
