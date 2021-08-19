import heapq
(n, m) = list(map(int, input().split()))
A = sorted([-int(x) for x in input().split()])
for _ in range(m):
    a = heapq.heappop(A)
    a = -(-a // 2)
    heapq.heappush(A, a)
print(-sum(A))
