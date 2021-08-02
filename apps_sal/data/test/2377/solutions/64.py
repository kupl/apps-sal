import heapq as hq
from itertools import accumulate
from math import ceil
N, H = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(N)]
ab.sort(key=lambda x: x[1], reverse=True)
ab.sort(key=lambda x: x[0], reverse=True)
ma, mb = ab[0]
q = [ab[i][1] for i in range(1, N)]
q.sort(reverse=True)
ans = float("inf")
acc = [0] + list(accumulate(q, lambda x, y: x + y))
for l in range(len(q) + 1):
    h = H
    cnt = l
    h -= acc[l]
    if h <= 0:
        ans = min(ans, cnt)
        continue
    h -= mb
    cnt += 1
    if h <= 0:
        ans = min(ans, cnt)
        continue
    cnt += ceil(h / ma)
    ans = min(ans, cnt)
print(ans)
