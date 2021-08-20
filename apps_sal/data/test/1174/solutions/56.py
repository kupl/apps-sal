import heapq
(N, M) = [int(x) for x in input().split()]
A = [-int(x) for x in input().split()]
heapq.heapify(A)
for i in range(M):
    a = heapq.heappop(A)
    heapq.heappush(A, -(-a // 2))
ans = -sum(A)
print(ans)
