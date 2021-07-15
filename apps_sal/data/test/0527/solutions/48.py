from collections import Counter, defaultdict
from bisect import bisect_right

s = input()
t = input()

c = Counter(s)
for e in t:
    if c[e] == 0:
        print((-1))
        return

ss = s + s
d = defaultdict(list)
for i, e in enumerate(ss):
    d[e].append(i)

now = -1
ans = 0
for e in t:
    i = bisect_right(d[e], now)
    nxt = d[e][i]
    ans += nxt - now
    now = nxt % len(s)

print(ans)

