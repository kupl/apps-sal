class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        profit = record = peeps = rots = i = 0
        n = len(customers)
        while peeps or i < n:
            if i < n:
                peeps += customers[i]
            board = min(4, peeps)
            profit += boardingCost * board - runningCost
            peeps -= board
            if profit > record:
                rots = i + 1
                record = profit
            i += 1
        return rots if rots != 0 else -1
