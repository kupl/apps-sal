class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        waiting = 0
        profit = []
        count = 0
        curr_profit = -1
        idx = 0
        total_people = 0
        res = -1
        while True:
            res = max(curr_profit, res)
            profit.append(curr_profit)
            if waiting <= 0 and idx > len(customers) - 1:
                break

            if idx > len(customers) - 1:
                people = 0
            else:
                people = customers[idx]
                idx += 1

            if waiting + people > 4:
                waiting = (waiting + people) - 4
                total_people += 4
            else:
                total_people += waiting + people
                if waiting > 0:
                    waiting -= (waiting + people)

            curr_profit = (total_people * boardingCost) - ((count + 1) * runningCost)
            count += 1
        if res < 0:
            return res
        else:
            for i, p in enumerate(profit):
                if p == res:
                    return i
