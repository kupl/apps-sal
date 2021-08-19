import heapq
(N, M) = map(int, input().split())
A = list(map(lambda x: int(x) * -1, input().split()))
heapq.heapify(A)
for i in range(M):
    t = heapq.heappop(A)
    heapq.heappush(A, -1 * (-t // 2))
print(-sum(A))
