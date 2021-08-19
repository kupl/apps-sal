class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        (s, e) = (1, max(piles))
        minK = float('inf')
        while s <= e:
            m = (s + e) // 2
            if self.eat(piles, m) > H:
                s = m + 1
            else:
                minK = min(minK, m)
                e = m - 1
        return minK

    def eat(self, piles, K):
        ret = 0
        for p in piles:
            ret += math.ceil(p / K)
        return ret
