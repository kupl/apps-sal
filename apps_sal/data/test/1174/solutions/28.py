from heapq import *
(N, M) = map(int, input().split())
A = list(map(lambda x: -int(x), input().split()))
heapify(A)
for m in range(M):
    heappush(A, int(heappop(A) / 2))
print(-sum(A))
