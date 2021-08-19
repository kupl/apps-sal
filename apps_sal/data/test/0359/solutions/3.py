def gcd(n, m):
    if m == 0:
        return n
    else:
        return gcd(m, n % m)


(a, h, w) = map(int, input().split())
g = gcd(a + h, a + w)
s = (a + w) // g
t = (w // a + 1) // s * s - 1
if t <= 0:
    print(-1)
else:
    print('%.10lf' % ((w - t * a) / (t + 1)))
