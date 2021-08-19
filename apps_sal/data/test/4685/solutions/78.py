import heapq
val = list(map(lambda x: -int(x), input().split()))
K = int(input())
heapq.heapify(val)
for i in range(K):
    v = heapq.heappop(val)
    heapq.heappush(val, v * 2)
print(-sum(val))
