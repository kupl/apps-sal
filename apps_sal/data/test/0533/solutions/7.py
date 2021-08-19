a1 = int(input())
a2 = int(input())
k1 = int(input())
k2 = int(input())
n = int(input())
p = a1 * (k1 - 1) + a2 * (k2 - 1)
if p >= n:
    print(0, end=' ')
else:
    print(n - p, end=' ')
s = 0
if k1 > k2:
    g = n // k2
    if g > a2:
        s += a2
        g = n - a2 * k2
        s += g // k1
        print(s)
    else:
        print(g)
else:
    g = n // k1
    if g > a1:
        s += a1
        g = n - a1 * k1
        s += g // k2
        print(s)
    else:
        print(g)
