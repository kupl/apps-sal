class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if boardingCost * 4 <= runningCost:
            return -1
        cum = 0
        best = float('-inf')
        bestturns = 0
        q = 0
        currturns = 0
        for (i, c) in enumerate(customers):
            q += c
            profit = min(4, q) * boardingCost - runningCost
            cum += profit
            if cum > best:
                best = cum
                bestturns = i + 1
            q = max(0, q - 4)
            currturns = i + 1
        while q > 0:
            profit = min(4, q) * boardingCost - runningCost
            cum += profit
            if cum > best:
                best = cum
                bestturns = currturns + 1
            q = max(0, q - 4)
            currturns += 1
        if best > 0:
            return bestturns
        return -1
