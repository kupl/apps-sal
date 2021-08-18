import math
import heapq

n, m = map(int, input().split())
a = list(map(lambda x: int(x) * -1, input().split()))

heapq.heapify(a)
for i in range(m):
    heapq.heappush(a, math.ceil(heapq.heappop(a) / 2))

print(int(-1 * sum(a)))
