import heapq
N, M = map(int, input().split())

A = list(map(int, input().split()))

for i in range(N):
    A[i] *= -1
heapq.heapify(A)
for i in range(M):
    n = heapq.heappop(A)
    heapq.heappush(A, -((-n) // 2))
print(-sum(A))
