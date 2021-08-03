class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        curr_arrive_idx = 0
        curr_wait = customers[0]
        curr_profit = []
        while(curr_wait > 0 or curr_arrive_idx < len(customers)):
            if(curr_wait > 4):
                curr_wait -= 4
                onboard = 4
            else:
                onboard = curr_wait
                curr_wait = 0
            if(len(curr_profit) == 0):
                curr_profit.append(onboard * boardingCost - runningCost)
            else:
                curr_profit.append(curr_profit[-1] + (onboard * boardingCost - runningCost))
            curr_arrive_idx += 1
            if(curr_arrive_idx < len(customers)):
                curr_wait += customers[curr_arrive_idx]

        max_profit = 0
        optimal_rotation = 0
        for idx, profit in enumerate(curr_profit):
            if(profit > max_profit):
                max_profit = profit
                optimal_rotation = idx + 1
        if(max_profit <= 0):
            return -1
        return optimal_rotation
