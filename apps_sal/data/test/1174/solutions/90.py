import heapq

n, m = map(int, input().split())
a = list(map(int, input().split()))

a = list(map(lambda x: -x, a))
heapq.heapify(a)
for _ in range(m):
    heapq.heappush(a, -((-heapq.heappop(a))//2))
print(-sum(a))
