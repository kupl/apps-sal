import heapq
N, M = list(map(int, input().split()))
hq = []
for price in map(int, input().split()):
    heapq.heappush(hq, -price)

for i in range(M):
    p = -heapq.heappop(hq)
    p /= 2
    heapq.heappush(hq, -p)

result = -sum([int(p) for p in hq])
print(result)
