from math import gcd
(n, x) = map(int, input().split())
m = [x] + list(map(int, input().split()))
m.sort()
if n == 1:
    print(m[1] - m[0])
else:
    res = gcd(m[1] - m[0], m[2] - m[1])
    for i in range(1, n - 1):
        a = m[i + 1] - m[i]
        b = m[i + 2] - m[i + 1]
        if res >= gcd(a, b):
            if res % gcd(a, b) == 0:
                res = gcd(a, b)
            else:
                res = gcd(res, gcd(a, b))
        elif gcd(a, b) % res != 0:
            res = gcd(res, gcd(a, b))
    print(res)
