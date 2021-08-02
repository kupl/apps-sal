import heapq
n, m = map(int, input().split())
a = list(map(int, input().split()))
a = list(map(lambda x: x * (-1), a))
heapq.heapify(a)
for i in range(m):
    x = heapq.heappop(a) * (-1) // 2
    heapq.heappush(a, (x * (-1)))
print(sum(a) * (-1))
