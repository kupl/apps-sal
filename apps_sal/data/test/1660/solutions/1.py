from sys import *
a = list(map(int, stdin.read().split()))
n = a[0]
m = a[1]
inf = 10 ** 5 + 1
g = [[] for i in range(inf)]
for i in range(2, len(a), 3):
    (b, c, w) = a[i:i + 3]
    g[w].append((c, b))
n += 1
s = [0] * n
for l in g:
    for (i, k) in [(i, s[j]) for (i, j) in l]:
        s[i] = max(s[i], k + 1)
print(max(s))
