(n,), *t = [[*map(int, t.split())]for t in open(0)]
e = [f := 0] * n * 4
for a, b in t:
    for j in range(n):
        c, d = t[j]; f |= d > 0 < a < c < b > b - a != d - c
        if b > c > a > 0 > d: t[j] = c, c + b - a
for a, b in t: e[a] += 1; e[b] += 1
print('YNeos'[f + max(e[:-1]) > 1::2])
