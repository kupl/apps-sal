from fractions import gcd
(a, b) = [int(x) for x in input().split()]
(c, d) = [int(x) for x in input().split()]
g = gcd(a, c)
if abs(b - d) % g != 0:
    print(-1)
else:
    s1 = set([b])
    s2 = set([d])
    while True:
        if b in s2:
            print(b)
            break
        if d in s1:
            print(d)
            break
        b += a
        d += c
        s1.add(b)
        s2.add(d)
