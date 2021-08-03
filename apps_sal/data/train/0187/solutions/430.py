class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:

        if sum(customers) == 0 or boardingCost * 4 <= runningCost:
            return -1
        no_loss = int(runningCost / boardingCost)
        money = []
        i = 0
        current_customer = 0

        while i < len(customers) or current_customer > 0:
            if i < len(customers):
                current_customer += customers[i]
            people = min(current_customer, 4)
            current_customer -= people

            money.append(boardingCost * people - runningCost)
            i = i + 1

        res = []
        ok = 0
        for i in range(len(money)):
            ok += money[i]
            res.append(ok)
        return res.index(max(res)) + 1
