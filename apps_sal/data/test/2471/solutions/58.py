from itertools import product
from collections import Counter

H, W, N = map(int, input().split())
V = set([tuple(map(int, input().split())) for _ in range(N)])
D = tuple(product((-1, 0, 1), repeat=2))

A = set()
cnt = Counter()
for a, b in V:
    for h, w in D:
        if 2 <= a + h <= H - 1 and 2 <= b + w <= W - 1:
            cnt[(a + h, b + w)] += 1

ans = [0] * 10
for c in cnt.values():
    ans[c] += 1

ans[0] = (H - 2) * (W - 2) - sum(ans)
print(*ans, sep='\n')
