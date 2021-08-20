from heapq import heappop, heappush
from collections import defaultdict
(N, M) = map(int, input().split())
D = defaultdict(list)
for _ in range(N):
    (A, B) = map(int, input().split())
    D[A].append(B)
H = []
ans = [0] * (M + 1)
for i in range(1, M + 1):
    for j in D[i]:
        heappush(H, -j)
    if H:
        a = heappop(H)
        ans[i] = -a
print(sum(ans))
