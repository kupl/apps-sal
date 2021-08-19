from itertools import accumulate
from bisect import bisect
n = int(input())
a = list(map(int, input().split()))
ans = 10 ** 9
cs = [0] + list(accumulate(a))
for i in range(2, n - 1):
    left = cs[i]
    right = cs[-1] - cs[i]
    lm = bisect(cs, left // 2)
    (l1, l2) = (cs[lm], left - cs[lm])
    (l3, l4) = (cs[lm - 1], left - cs[lm - 1])
    if abs(l1 - l2) > abs(l3 - l4):
        l1 = l3
        l2 = l4
    rm = bisect(cs, left + right // 2)
    (r1, r2) = (cs[rm] - cs[i], right - (cs[rm] - cs[i]))
    (r3, r4) = (cs[rm - 1] - cs[i], right - (cs[rm - 1] - cs[i]))
    if abs(r1 - r2) > abs(r3 - r4):
        r1 = r3
        r2 = r4
    ans = min(ans, max(l1, l2, r1, r2) - min(l1, l2, r1, r2))
print(ans)
