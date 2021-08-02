import math

a, b = list(map(int, input().split()))
c, d = list(map(int, input().split()))

g = math.gcd(a, c)
if (d - b) % g != 0:
    print(-1)
else:
    t0, t1 = b, d
    while t0 != t1:
        if t0 < t1:
            t0 += a
        else:
            t1 += c
    print(t0)
