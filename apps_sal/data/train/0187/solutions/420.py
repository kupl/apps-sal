class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        p1 = 4 * boardingCost - runningCost
        n = 0
        pn = 0
        res = [0, 0]
        w = 0

        if p1 <= 0:
            return -1

        for c in customers:
            if w + c >= 4:
                n += 1
                pn += p1
                w += c - 4
                res = self.comp(res, pn, n)
            else:
                pn += (w + c) * boardingCost - runningCost
                n += 1
                res = self.comp(res, pn, n)
                w = 0
        n += w // 4
        pn += (w // 4) * p1
        ps = (w % 4) * boardingCost - runningCost
        if ps > 0:
            pn += ps
            n += 1
        res = self.comp(res, pn, n)
        return res[1]

    def comp(self, res, pn, n):
        if res[0] < pn:
            res = [pn, n]
        return res
