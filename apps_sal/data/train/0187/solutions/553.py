class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        nwaiting = 0
        profit = 0
        maxprofit = 0
        res = -1
        for (i, c) in enumerate(customers, 1):
            nwaiting += c
            onboard = min(4, nwaiting)
            nwaiting -= onboard
            profit += onboard * boardingCost - runningCost
            if maxprofit < profit:
                maxprofit = profit
                res = i
        if nwaiting > 0:
            roundn = nwaiting // 4
            nwaiting -= roundn * 4
            profit += roundn * (4 * boardingCost - runningCost)
            if maxprofit < profit:
                maxprofit = profit
                res += roundn
        if nwaiting > 0:
            profit += nwaiting * boardingCost - runningCost
            if maxprofit < profit:
                maxprofit = profit
                res += 1
        return res if maxprofit > 0 else -1
