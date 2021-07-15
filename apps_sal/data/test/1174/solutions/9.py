import heapq, math

n, m = map(int, input().split())
A = list(map(int, input().split()))
a = list(map(lambda x: x*(-1), A))
heapq.heapify(a)
for i in range(m):
    max_a = heapq.heappop(a)
    heapq.heappush(a, math.ceil(max_a/2))
print(-sum(a))
