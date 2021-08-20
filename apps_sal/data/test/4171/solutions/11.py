"""input
5 3
1 2 3 3 3
"""
from collections import defaultdict as dd
(n, k) = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
d = dd(list)
for x in a:
    i = 0
    while x:
        d[x].append(i)
        x //= 2
        i += 1
ans = 999999999999
for i in d:
    if len(d[i]) >= k:
        d[i].sort()
        ans = min(ans, sum(d[i][0:k]))
print(ans)
