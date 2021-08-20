from math import ceil as c
from math import log2 as l
(n, k) = map(int, input().split())
(ans, m) = (0, 1 / n)
for i in range(1, n + 1):
    if i < k:
        ans += 0.5 ** c(l(k / i)) * m
    else:
        ans += m
print(ans)
