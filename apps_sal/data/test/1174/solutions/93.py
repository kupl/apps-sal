import heapq
(N, M) = [int(_) for _ in input().split()]
A = [int(_) * -1 for _ in input().split()]
heapq.heapify(A)
for i in range(M):
    a = heapq.heappop(A) * -1
    heapq.heappush(A, -1 * (a // 2))
print(-1 * sum(A))
