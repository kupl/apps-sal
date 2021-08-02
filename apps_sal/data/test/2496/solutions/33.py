from math import gcd
n, *a = map(int, open(0).read().split())
g = 0
for i in a:
    g = gcd(g, i)
    if g == 1:
        break
else:
    print("not coprime")
    return
m = 10**6 + 1
d = [i for i in range(m)]
for i in range(4, m, 2):
    d[i] = 2
p = 3
while p**2 < m:
    if d[p] == p:
        for i in range(3 * p, m, 2 * p):
            if d[i] == i:
                d[i] = p
    p += 2
p = set()
for i in a:
    t = set()
    while i > 1:
        t.add(d[i])
        i //= d[i]
    if p & t:
        print("setwise coprime")
        return
    else:
        p |= t
print('pairwise coprime')
