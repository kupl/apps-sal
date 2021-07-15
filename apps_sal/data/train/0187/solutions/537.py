class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        wt = 0
        profit = 0
        bp = 0
        ret = -1
        cr = 0
        gondola = [0, 0, 0, 0]
        i = 0
        while i < len(customers) or wt:
            cr += 1
            if i < len(customers):
                e = customers[i]
                wt += e
            if wt:
                take = min(wt, 4)
                profit += boardingCost * take - runningCost
                wt -= take
                gondola = gondola[1:] + [take]
            else:
                if sum(gondola) == 0:
                    profit -= runningCost
            if profit > bp:
                bp = profit
                ret = cr
            i += 1
        return ret

