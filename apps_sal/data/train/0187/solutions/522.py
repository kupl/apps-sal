class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        left_people = 0
        profit = 0
        maxProfit = -1
        maxpc = 0
        counter = 0
        i = 0
        while i < len(customers) or left_people > 0:
            counter += 1
            left_people += customers[i] if i < len(customers) else 0
            profit += min(left_people, 4) * boardingCost - runningCost
            left_people = max(left_people - 4, 0)
            if profit > maxProfit:
                maxProfit = profit
                maxpc = counter
            i += 1
        return -1 if maxProfit < 0 else maxpc
