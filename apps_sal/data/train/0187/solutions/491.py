class Solution:
    def minOperationsMaxProfit(self, customers, boardingCost: int, runningCost: int) -> int:
        rt, rp = -1, 0
        N = len(customers)
        i, wpp, tpp = 0, 0, 0
        time = 1
        while i < N or wpp > 0:
            if i < N:
                wpp += customers[i]
                i += 1
            tpp += min(4, wpp)
            wpp -= 4
            wpp = max(wpp, 0)
            tmp = tpp * boardingCost - time * runningCost
            if tmp > rp:
                rp = tmp
                rt = time
            time += 1
        return rt

