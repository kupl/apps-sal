import heapq
(N, M) = list(map(int, input().split()))
A = list(map(int, input().split()))
A = list([x * -1 for x in A])
heapq.heapify(A)
for _ in range(M):
    heapq.heappush(A, -1 * (heapq.heappop(A) * -1 // 2))
print(sum(A) * -1)
