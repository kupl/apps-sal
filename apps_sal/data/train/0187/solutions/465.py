class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        numWaiting = 0
        totalOnboard = 0
        totalRunningCost = 0
        maxProfit = 0
        ans = 0
        i = 0
        while numWaiting > 0 or i < len(customers):
            numWaiting += (customers[i] if i < len(customers) else 0)
            t = min(4, numWaiting)
            totalOnboard += t
            numWaiting -= t

            totalRunningCost += runningCost

            curProfit = totalOnboard * boardingCost - totalRunningCost
            if curProfit > maxProfit:
                ans = (i + 1)
                maxProfit = curProfit
            i += 1

        return ans if maxProfit > 0 else -1
