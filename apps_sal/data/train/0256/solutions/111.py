class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:

        k = sum(piles) // H
        if k == 0:
            return 1
        while True:
            h = 0
            prev = k
            for p in piles:
                print(p, k)
                if p > 1:
                    h += (p - 1) // k + 1
                else:
                    h += 1
                if h > H:
                    break
            if h <= H:
                return k
            k += 1
