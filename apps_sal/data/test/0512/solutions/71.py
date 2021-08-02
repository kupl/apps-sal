import sys
(n,), *t = [[*map(int, t.split())]for t in open(0)]
s = 'Yes'
for _ in t:
    for a, b in t:
        if min(a, b) < 0: continue
        for j, (c, d) in enumerate(t):
            if a < c < b and b - a != d - c < d > 0: s = 'No'
            if b > c > a > 0 > d: t[j] = c, c + b - a
            if a < d < b > 0 > c: t[j] = d - b + a, d
c = [0] * n * 4
for a, b in t:
    c[a] += 1
    c[b] += 1
print((s, 'No')[max(c[:n * 3]) > 1])
