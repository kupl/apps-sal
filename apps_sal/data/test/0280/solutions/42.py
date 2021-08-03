from itertools import permutations
from bisect import bisect_left
n, m = list(map(int, input().split()))
w = list(map(int, input().split()))
li = [list(map(int, input().split())) for _ in range(m)]
li.sort(key=lambda x: x[1])
l = [0] * (m + 1)
v = [0] * (m + 1)
for i in range(m):
    l[i + 1], v[i + 1] = li[i]
for i in range(m):
    l[i + 1] = max(l[i], l[i + 1])
if max(w) > min(v[1:]):
    print((-1))
else:
    dv = dict()
    for i in range(2 ** n):
        t = 0
        for j in range(n):
            if (i >> j) & 1:
                t += w[j]
        dv[t] = l[bisect_left(v, t) - 1]
    ans = 10 ** 18
    for p in permutations(w):
        li = [0] * (n + 1)
        for i in range(n):
            li[i + 1] = li[i] + p[i]
        x = [0] * n
        for i in range(n):
            for j in range(i + 1, n + 1):
                x[j - 1] = max(x[j - 1], x[i] + dv[li[j] - li[i]])
        ans = min(ans, x[-1])
    print(ans)
