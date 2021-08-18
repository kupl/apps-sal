import bisect
from collections import defaultdict

s = input()
t = input()
if set(s) & set(t) != set(t):
    print((-1))
    return
cnt = defaultdict(list)
for i, c in enumerate(s, 1):
    cnt[c].append(i)
loop = 0
prev = 0
for w in t:
    l = cnt[w]
    idx = bisect.bisect_right(l, prev)
    if idx < len(l):
        prev = l[idx]
    else:
        prev = l[0]
        loop += 1
ans = loop * len(s) + prev
print(ans)
