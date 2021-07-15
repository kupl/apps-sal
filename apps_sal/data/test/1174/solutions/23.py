import heapq
N, M = list(map(int, input().split()))
A = list([int(x)*(-1) for x in input().split()])
heapq.heapify(A)
for i in range(0,M):
    a=heapq.heappop(A)
    heapq.heappush(A,(-1)*(-a//2))
print((-sum(A)))

#　優先度付きキューが難しい

