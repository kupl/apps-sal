class Solution:

    def minOperationsMaxProfit(self, customers, boardingCost, runningCost):
        if boardingCost * 4 - runningCost < 0:
            return -1
        incomes = list()
        incomes.append(0)
        it = iter(customers)
        idx = 0
        while True:
            try:
                cnt = next(it)
                if cnt > 4:
                    if idx == len(customers) - 1:
                        customers.append(cnt - 4)
                    else:
                        customers[idx + 1] += cnt - 4
                    cnt = 4
                incomes.append(incomes[idx] + boardingCost * cnt - runningCost)
                idx += 1
            except StopIteration:
                break
        return incomes.index(max(incomes))
