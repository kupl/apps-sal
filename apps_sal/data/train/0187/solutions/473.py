class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        rotation = 0
        wait = profit = 0
        n = len(customers)
        gondola = [0]*4
        maxProfit, maxRotation = -1, -2
        while rotation < n or wait:
            if rotation < n:
                wait += customers[rotation]
            m = min(4, wait)
            wait = max(wait - m, 0)
            gondola[rotation%4] = m
            profit += boardingCost*m - runningCost
            if profit > maxProfit:
                maxProfit, maxRotation = profit, rotation
            rotation += 1
        return maxRotation + 1
