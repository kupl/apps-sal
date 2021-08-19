import math        # factorical（階乗) # hypot(距離)
import heapq
# from fractions import gcd # Python3.5以前 # lcm（最小公倍数） = (a*b)//gcd(a,b)
# from fractions import Fraction
# from math import gcd # Python3.6以降
# --------------------------------------------------------------

n, m = map(int, input().split())
price = list(map(int, input().split()))

price = [-i for i in price]

heapq.heapify(price)

for i in range(m):
    sm = heapq.heappop(price)
    sm = -(-sm // 2)
    heapq.heappush(price, sm)

price = [-i for i in price]

print(sum(price))
