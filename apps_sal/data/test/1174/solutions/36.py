import heapq
(n, m) = map(int, input().split())
a = list(map(int, input().split()))
a = [i * -1 for i in a]
heapq.heapify(a)
for i in range(m):
    x = -1 * heapq.heappop(a) // 2
    heapq.heappush(a, -x)
print(-sum(a))
