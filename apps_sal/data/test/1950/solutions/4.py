from heapq import *
n = int(input())
a = list(map(int, input().split()))
heap = []
res = 0
for i in range(n):
    heappush(heap, a[i])
if n % 2 == 0:
    heappush(heap, 0)
while n > 1:
    cur = heappop(heap)
    cur += heappop(heap)
    cur += heappop(heap)
    res += cur
    heappush(heap, cur)
    n -= 2
print(res)
