from collections import Counter as c
from itertools import product as p
(h, w, n) = map(int, input().split())
I = [list(map(int, input().split())) for i in [0] * n]
ans = [0] * 9
for (k, v) in c(c([(a - x) * w + b - y for (x, y) in p(range(3), repeat=2) for (a, b) in I if h - 1 > a - x > 0 < b - y < w - 1]).values()).items():
    ans[k - 1] = v
print((h - 2) * (w - 2) - sum(ans), *ans, sep='\n')
