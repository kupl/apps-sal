from collections import defaultdict
from itertools import product

H, W, N = map(int, input().split())
cnt = defaultdict(int)
D = tuple(product((-1, 0, 1), repeat=2))

for _ in range(N):
    a, b = map(int, input().split())
    for dh, dw in D:
        h = a + dh
        w = b + dw
        if 2 <= h <= H - 1 and 2 <= w <= W - 1:
            cnt[(h, w)] += 1

ans = [0] * 10
for c in cnt.values():
    ans[c] += 1
ans[0] = (H - 2) * (W - 2) - sum(ans)
print(*ans, sep='\n')
