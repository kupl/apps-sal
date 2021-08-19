import math
import heapq
(n, m) = map(int, input().split())
price = list(map(int, input().split()))
price = [-i for i in price]
heapq.heapify(price)
for i in range(m):
    sm = heapq.heappop(price)
    sm = -(-sm // 2)
    heapq.heappush(price, sm)
price = [-i for i in price]
print(sum(price))
