class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        rotate = left = 0
        ans = -1
        profit = maxprofit = 0
        for cnt in customers:
            cnt += left
            rotate += 1
            left = max(0, cnt - 4)
            profit += boardingCost * min(4, cnt) - runningCost
            if profit > maxprofit:
                maxprofit = profit
                ans = rotate
        while left > 0:
            rotate += 1
            profit += boardingCost * min(4, left) - runningCost
            if profit > maxprofit:
                maxprofit = profit
                ans = rotate
            left -= 4
        return ans
