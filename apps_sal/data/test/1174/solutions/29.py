import heapq
(n, m) = map(int, input().split())
a = list(map(int, input().split()))
a = list(map(lambda x: x * -1, a))
heapq.heapify(a)
for i in range(m):
    b = heapq.heappop(a)
    heapq.heappush(a, -(-b // 2))
print(sum(a) * -1)
