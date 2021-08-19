import heapq
(N, M) = list(map(int, input().split()))
A = list([int(x) * -1 for x in input().split()])
heapq.heapify(A)
for _ in range(M):
    temp_min = heapq.heappop(A)
    heapq.heappush(A, -1 * (temp_min * -1 // 2))
print(-sum(A))
