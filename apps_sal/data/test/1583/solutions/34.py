import math
a, b, x = list(map(int, input().split()))

if x/a < a*b/2:
    print(math.atan(a*b*b/(2*x))*180/math.pi)
else:
    print(math.atan(2/a * (b-x/a**2))*180/math.pi)
