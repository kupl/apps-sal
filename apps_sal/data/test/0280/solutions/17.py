from bisect import bisect_left
from itertools import permutations
n, m = map(int, input().split())
w = list(map(int, input().split()))
lv = [list(map(int, input().split()))[::-1] for i in range(m)]
lv.sort()
l, v = [l_ for v_, l_ in lv], [v_ for v_, l_ in lv]
if max(w) > min(v):print(-1);return()
for i in range(1, m):
    l[i] = max(l[i - 1], l[i])
l.append(0)
ans = float("inf")
for p in permutations(range(n), r=n):
    w2 = [w[w_] for w_ in p]
    lis = [0]
    now = w2[0]
    for i in range(1, n):
        now += w2[i]
        cur = now
        cnt = 0
        for j in range(i):
            ind = bisect_left(v, cur) - 1
            cnt = max(cnt, lis[j] + l[ind])
            cur -= w2[j]
        lis.append(cnt)
    ans = min(ans, lis[-1])
print(ans)
