from heapq import heapify, heappop, heappush
(N, M) = map(int, input().split())
A = [[] for _ in range(M + 1)]
for i in range(N):
    (a, b) = map(int, input().split())
    if a <= M:
        A[a].append(b)
ans = 0
L = []
for day in range(1, M + 1):
    for t in A[day]:
        heappush(L, -t)
    if not L:
        continue
    temp = heappop(L)
    ans += -temp
print(ans)
