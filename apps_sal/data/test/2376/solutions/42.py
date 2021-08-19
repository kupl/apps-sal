from collections import defaultdict
import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
mod = 10 ** 9 + 7
INF = 10 ** 18
eps = 10 ** (-7)
(N, W) = list(map(int, readline().split()))
goods = [tuple(map(int, readline().split())) for i in range(N)]
d = defaultdict(int)
d[0] = 0
for (w, v) in goods:
    dnew = defaultdict(int)
    for (key, value) in list(d.items()):
        dnew[key] = value
    for (key, value) in list(d.items()):
        dnew[key + w] = max(dnew[key + w], d[key] + v)
    d = dnew
ans = 0
for (k, v) in list(d.items()):
    if k <= W:
        ans = max(ans, v)
print(ans)
