((n,), *t) = [[*map(int, t.split())] for t in open(0)]
e = [(f := 0)] * n * 4
for (a, b) in t:
    j = 0
    for (c, d) in t:
        f |= d > 0 < a < c < b > b - a != d - c
        t[j] = (c, (d, c + b - a)[b > c > a > d])
        j += 1
for (a, b) in t:
    e[a] += 1
    e[b] += 1
print('YNeos'[f + max(e[:-1]) > 1::2])
