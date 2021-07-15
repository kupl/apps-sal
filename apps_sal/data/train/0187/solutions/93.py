class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        maxProfit = (-1, -1)
        customerWaiting = 0
        customerBoarded = 0
        rounds = 0
        profit = 0
        for i in range(0, len(customers)):
            customerWaiting+= customers[i]
            rounds+=1
            # print(\"########\")
            # print(f\"Customer Waiting: {customerWaiting} rounds: {rounds}\")
            if customerWaiting >= 4:
                customerWaiting-=4
                customerBoarded+=4
                profit = ((boardingCost * customerBoarded) - (rounds*runningCost))
            else:
                customerBoarded+=customerWaiting
                profit = ((boardingCost * customerBoarded) - (rounds*runningCost))
                customerWaiting=0
            if maxProfit[0] < profit:
                    maxProfit = (profit, rounds)
            # print(f\"Current Profit: {profit} Maximum Profit: {maxProfit}\")
            
        while customerWaiting > 0:
            rounds+=1
            # print(\"########\")
            # print(f\"Customer Waiting: {customerWaiting} rounds: {rounds}\")
            if customerWaiting >= 4:
                customerWaiting-=4
                customerBoarded+=4
                profit = ((boardingCost * customerBoarded) - (rounds*runningCost))
            else:
                customerBoarded+=customerWaiting
                profit = ((boardingCost * customerBoarded) - (rounds*runningCost))
                customerWaiting=0
            if maxProfit[0] < profit:
                    maxProfit = (profit, rounds)
            # print(f\"Current Profit: {profit} Maximum Profit: {maxProfit}\")
        if maxProfit[0] >= 0:
            return maxProfit[1]
        return -1
