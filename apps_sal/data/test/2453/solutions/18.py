from collections import *
n = int(input())
d = defaultdict(int)
for _ in [0] * n:
    (l, r) = list(map(int, input().split()))
    d[l] += 1
    d[r + 1] -= 1
s = p = 0
f = [0] * (n + 1)
for (k, v) in sorted(d.items()):
    f[s] += k - p
    s += v
    p = k
print(*f[1:])
