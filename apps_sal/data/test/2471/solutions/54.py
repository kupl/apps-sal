from collections import Counter as co
from itertools import product as pr
(h, w, n) = map(int, input().split())
ans = [(h - 2) * (w - 2)] + [0] * 9
io = [tuple(map(int, input().split())) for i in range(n)]
for (k, v) in co(co([(a - x) * w + b - y for (x, y) in pr(range(3), repeat=2) for (a, b) in io if h - 1 > a - x > 0 < b - y < w - 1]).values()).items():
    ans[k] = v
    ans[0] -= v
print(*ans, sep='\n')
