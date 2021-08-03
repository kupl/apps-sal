import heapq

N, M = map(int, input().split())
jobs = [[] for i in range(M)]

for i in range(N):
    A, B = map(int, input().split())
    if A - 1 < M:
        jobs[A - 1].append(B)

q = []
heapq.heapify(q)
ans = 0
for i in range(M):
    for j in jobs[i]:
        heapq.heappush(q, -j)
    if len(q) != 0:
        ans += -heapq.heappop(q)

print(ans)
