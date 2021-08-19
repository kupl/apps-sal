import heapq
import math
(n, m) = map(int, input().split())
a = list(map(lambda x: int(x) * -1, input().split()))
heapq.heapify(a)
for i in range(m):
    x = heapq.heapreplace(a, math.ceil(a[0] / 2))
print(sum(a) * -1)
