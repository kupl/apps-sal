import heapq
import sys
N, M = map(int, input().split())
B = [[] for _ in range(M + 1)]
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    if a <= M:
        B[a].append(b)

ans = 0
q = []
for i in range(1, M + 1):
    for b in B[i]:
        heapq.heappush(q, -b)
    if q:
        ans += -(heapq.heappop(q))
print(ans)
