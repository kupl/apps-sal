class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        wait = total = profit = maxp = res = i = 0
        while wait or i < len(customers):
            if i < len(customers):
                total += customers[i]
                wait = max(0, customers[i] + wait - 4)
            else:
                wait = max(0, wait - 4)
            i += 1
            profit = boardingCost * (total - wait) - runningCost * i
            if profit > maxp:
                maxp, res = profit, i
        return res if maxp > 0 else -1
