class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        numWaiting = 0
        totalOnboard = 0
        totalRunningCost = 0
        maxProfit = 0
        ans = 0
        i = 0
        # for i in range(len(customers)):
        while numWaiting > 0 or i < len(customers):
            numWaiting += (customers[i] if i < len(customers) else 0)
            t = min(4, numWaiting)
            totalOnboard += t
            numWaiting -= t

            totalRunningCost += runningCost

            curProfit = totalOnboard * boardingCost - totalRunningCost
            #maxProfit = max(curProfit, maxProfit)
            #print(i + 1, curProfit)
            if curProfit > maxProfit:
                ans = (i + 1)
                maxProfit = curProfit
            i += 1

        #print('ans', ans)
        return ans if maxProfit > 0 else -1
