import operator
from collections import defaultdict
from functools import reduce
n = int(input())
arr = [input() for _ in range(n)]
l = list(reduce(operator.and_, [set(i) for i in arr]))
d = defaultdict(lambda: 1 << 60)
l.sort()
for s in arr:
    for c in l:
        cnt = s.count(c)
        d[c] = min(d[c], cnt)
res = []
for (k, v) in d.items():
    res.append(k * v)
ans = ''.join(res)
print(ans)
