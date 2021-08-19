import heapq
(N, M) = list(map(int, input().split()))
A = list([int(x) * -1 for x in input().split()])
heapq.heapify(A)
for _ in range(M):
    tmp = heapq.heappop(A)
    tmp = -tmp // 2
    heapq.heappush(A, -tmp)
print(-sum(A))
