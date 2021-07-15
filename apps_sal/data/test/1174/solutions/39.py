import heapq
import sys

lines = sys.stdin.readlines()

N, M = [int(n) for n in lines[0].strip().split()]
prices = [-int(n) for n in lines[1].strip().split()]

heapq.heapify(prices)

for _ in range(M):
    price = -heapq.heappop(prices)
    heapq.heappush(prices, -1 * (price // 2))

print(-sum(prices))
