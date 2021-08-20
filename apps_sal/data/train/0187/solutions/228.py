class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:

        def cal(k, p):
            if k == 0:
                p = p
            else:
                p += k * boardingCost - runningCost
            return p
        ans = 0
        p = 0
        w = 0
        i = 0
        itop = -1
        for n in customers:
            i += 1
            w += n
            k = min(4, w)
            p = cal(k, p)
            if ans < p:
                ans = p
                itop = i
            w -= k
        while w:
            i += 1
            k = min(4, w)
            p = cal(k, p)
            if ans < p:
                ans = p
                itop = i
            w -= k
        return itop
