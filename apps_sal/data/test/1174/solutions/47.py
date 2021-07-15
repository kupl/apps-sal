import heapq
N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
A = [-a for a in A]
heapq.heapify(A)

for i in range(M):
    most_expensive = -heapq.heappop(A)
    most_expensive //= 2
    heapq.heappush(A, -most_expensive)

print((-sum(A)))



