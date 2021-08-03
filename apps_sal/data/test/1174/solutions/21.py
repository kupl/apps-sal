from heapq import *

n, m = map(int, input().split())
A = list(map(lambda x: int(x) * (-1), input().split()))
heapify(A)

for _ in range(m):
    max_a = heappop(A) * (-1)
    max_a //= 2
    heappush(A, -max_a)
print(-sum(A))
