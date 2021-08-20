from heapq import heappop, heappush, heapify
(n, m) = map(int, input().split())
arr = list(map(int, input().split()))
arr = [-x for x in arr]
heapify(arr)
for _ in range(m):
    a = heappop(arr)
    heappush(arr, -(-a // 2))
print(-sum(arr))
