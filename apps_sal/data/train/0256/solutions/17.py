import math


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        L = len(piles)
        if L == H:
            return max(piles)
        k2 = max(piles)
        k1 = 1
        res = k2
        k = k1
        while k1 < k2 - 1:

            cur = 0
            for j in range(L):
                cur += math.ceil(piles[j] / k)
                if cur > H:
                    k1 = k
                    break
            if cur <= H:
                k2 = k
                res = min(res, k)
            # print(k1,k2,k,cur)
            k = (k1 + k2) // 2
        return res
