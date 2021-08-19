class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        (r, p) = (-1, 0)
        rc = 0
        oc = 0
        d = 0
        for (i, c) in enumerate(customers):
            d = i + 1
            rc += c
            oc = min(4, rc) + oc
            rc = max(rc - 4, 0)
            cp = oc * boardingCost - (i + 1) * runningCost
            if cp > p:
                p = cp
                r = i + 1
        while rc > 0:
            d += 1
            oc = min(4, rc) + oc
            rc = max(rc - 4, 0)
            cp = oc * boardingCost - d * runningCost
            if cp > p:
                p = cp
                r = d
        return r
