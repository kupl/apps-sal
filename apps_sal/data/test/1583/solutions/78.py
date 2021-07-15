import math
a, b, x = map(int, input().split())
if x>=pow(a,2)*b/2:
    print(math.degrees(math.atan(2*(pow(a,2)*b-x)/pow(a,3))))
else:
    print(math.degrees(math.atan(a*pow(b,2)/(2*x))))
