class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        q_len = current_profit = 0
        max_profit = ans = -1
        for (rotation, new_people) in enumerate(customers):
            q_len += new_people
            current_profit += boardingCost * min(4, q_len) - runningCost
            if current_profit > max_profit:
                max_profit = current_profit
                ans = rotation + 1
            q_len = max(0, q_len - 4)
        rotation = len(customers)
        while q_len > 0:
            current_profit += boardingCost * min(4, q_len) - runningCost
            if current_profit > max_profit:
                max_profit = current_profit
                ans = rotation + 1
            q_len = max(0, q_len - 4)
            rotation += 1
        return ans
