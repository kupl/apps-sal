class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        people = 0
        on = 0
        i = 0
        money = 0
        ans = -1
        j = 0
        for c in customers:
            people += c
            i += 1
            x = min(people, 4)
            on += x
            people -= x
            money = on * boardingCost - runningCost * i
            if money > ans:
                j = i
                ans = money

        while people:
            i += 1
            x = min(people, 4)
            on += x
            people -= x
            money = on * boardingCost - runningCost * i
            if money > ans:
                j = i
                ans = money

        return j if ans > 0 else -1
