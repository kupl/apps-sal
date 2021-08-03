from fractions import Fraction
from heapq import *


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:

        # quality = [3,1,10,10,1]
        # wage = [4,8,2,2,7]
        # K = 3

        workers = sorted((Fraction(w, q), q, w) for q, w in zip(quality, wage))

        # print(workers)

        result = float('inf')
        maxheap = []
        current_sum = 0
        for ratio, q, w in workers:
            heappush(maxheap, -q)
            current_sum += q

            if len(maxheap) > K:
                current_sum += heappop(maxheap)

            if len(maxheap) == K:
                result = min(result, ratio * current_sum)

            # print(ratio, q, w, maxheap,current_sum,result)

        return float(result)


#         from fractions import Fraction
#         ans = float('inf')

#         N = len(quality)
#         for captain in range(N):
#             # Must pay at least wage[captain] / quality[captain] per qual
#             factor = Fraction(wage[captain], quality[captain])
#             prices = []
#             for worker in range(N):
#                 price = factor * quality[worker]
#                 if price >= wage[worker]:
#                     prices.append(price)

#             if len(prices) >= K:
#                 prices.sort()
#                 ans = min(ans, sum(prices[:K]))

#         return float(ans)
