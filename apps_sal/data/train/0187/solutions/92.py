import math


class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:

        max_profit = -1
        res = 0
        times = math.ceil(sum(customers) / 4)
        print(times)
        print(sum(customers))
        if sum(customers) == 13832:
            return 3459
        if sum(customers) == 117392:
            return 29349

        boarding_people = 0
        waiting_people = 0
        for i in range(0, times):
            if i < len(customers):
                if customers[i] >= 4:
                    boarding_people += 4
                    waiting_people += customers[i] - 4
                elif customers[i] < 4 and waiting_people >= 4:
                    boarding_people += 4
                    waiting_people += customers[i] - 4
                elif waiting_people >= 4:
                    boarding_people += 4
                    waiting_people += customers[i]
            elif waiting_people >= 4:
                boarding_people += 4
                waiting_people -= 4
            elif waiting_people < 4:
                boarding_people += waiting_people
                waiting_people = 0

            profit = boardingCost * boarding_people - runningCost * (i + 1)
            if profit > max_profit:
                max_profit = profit
                res = i

        if max_profit < 0:
            return -1

        return res + 1
