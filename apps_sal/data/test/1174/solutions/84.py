import heapq
(N, M) = list(map(int, input().split()))
A = list([-int(x) for x in input().split()])
heapq.heapify(A)
for _ in range(M):
    p = -heapq.heappop(A)
    tmp = p // 2
    heapq.heappush(A, -tmp)
print(-sum(A))
