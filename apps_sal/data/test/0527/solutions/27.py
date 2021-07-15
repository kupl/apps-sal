from collections import defaultdict
from bisect import bisect_left
s = input()
t = input()
ids = defaultdict(list)
for i, c in enumerate(s):
    ids[c].append(i)
i = 0
ans = 0
for c in t:
    if c not in ids:
        print(-1)
        return
    ls = ids[c]
    j = bisect_left(ls, i)
    if j == len(ls):
        ans += len(s)
        i = ls[0]+1
    else:
        i = ls[j]+1
print(ans+i)
