def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


(a, h, w) = list(map(int, input().split()))
g = gcd(a + h, a + w)
t = (a + w) // g
q = (w // a + 1) // t * t - 1
if q <= 0:
    print(-1)
else:
    print('%.9lf' % ((w - q * a) / (q + 1)))
