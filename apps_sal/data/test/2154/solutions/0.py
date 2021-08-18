from heapq import *

N = int(input())
price = [int(i) for i in input().split()]

total = 0
inf = (10**6) + 1
h = [inf]

for p in price:
    if p > h[0]:
        total += (p - heappop(h))
        heappush(h, p)
    heappush(h, p)

print(total)
