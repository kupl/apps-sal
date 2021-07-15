import heapq
N,M = map(int,input().split())
lsA = list(map(int,input().split()))
lsA = [-i for i in lsA]
heapq.heapify(lsA)
for i in range(M):
    maxA = heapq.heappop(lsA)
    heapq.heappush(lsA,-(-maxA//2))
lsA = [-i for i in lsA]
print(sum(lsA))
