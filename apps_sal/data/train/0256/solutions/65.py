class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        if H == len(piles):
            return max(piles)
        elif sum(piles) <= H:
            return 1
        cntr = collections.Counter(piles)
        lst = set()
        for key in cntr.keys():
            lst.add((key, cntr[key]))
        s = 2
        e = max(piles) - 1
        while s <= e:
            K = int((s + e) / 2)
            total = 0
            for (pile, n) in lst:
                (q, r) = divmod(pile, K)
                if r:
                    total += (q + 1) * n
                else:
                    total += q * n
                if total > H:
                    break
            if total <= H:
                e = K - 1
            else:
                s = K + 1
        return s
