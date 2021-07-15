import math

a, b, x = list(map(int, input().split()))
v = a*a*b
if v == x:
    print((0))
elif v/2 <= x < v:
    h = 2*(v-x)/a**2
    ans = math.atan(h/a)
    print((math.degrees(ans)))
else:
    h = 2*x/(b*a)
    ans = math.atan(h/b)
    print((90-math.degrees(ans)))

