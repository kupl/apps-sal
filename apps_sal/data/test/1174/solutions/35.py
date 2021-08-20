import heapq
(N, M) = map(int, input().split())
A = list(map(int, input().split()))
A = [a * -1 for a in A]
heapq.heapify(A)
for _ in range(M):
    a = heapq.heappop(A)
    heapq.heappush(A, -(-a // 2))
print(sum(A) * -1)
