from itertools import accumulate
import math
n = int(input())
p = [int(x) for x in input().split()]
S1 = sum(p)
d = [x == 'A' for x in input()]
for i in range(n):
    if d[i]:
        p[i] = -p[i]
prefix = list(accumulate([0] + p))
S = prefix[-1]
(m, M) = (min(prefix), max(prefix))
print((S1 + max(S - 2 * m, 2 * M - S)) // 2)
