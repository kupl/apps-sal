class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if boardingCost * 4 <= runningCost:
            return -1
        customers.append(0)
        profit = []
        curProfit, runs = 0, 0
        for i in range(len(customers) - 1):
            if customers[i] >= 4:
                if i + 1 < len(customers):
                    customers[i + 1] += customers[i] - 4
                customers[i] = 4
            if customers[i] * boardingCost < runningCost:
                runs = runs + 1
                profit.append((curProfit, runs))
                continue
            curProfit += customers[i] * boardingCost - runningCost
            runs += 1
            profit.append((curProfit, runs))
        #print(customers, curProfit, runs)
        if customers[-1] > 0:
            runs = runs + (customers[-1] // 4)
            curProfit += (customers[-1] // 4) * boardingCost - (customers[-1] // 4) // 4 * runningCost
            customers[-1] = customers[-1] % 4
            if customers[-1] * boardingCost > runningCost:
                runs = runs + 1
                curProfit += customers[-1] * boardingCost - runningCost
            # print(\"w\", curProfit, runs)
            profit.append((curProfit, runs))
        profit.sort(key=lambda x: (-x[0], x[1]))
        # print(profit)
        return profit[0][1] if profit[0][0] > 0 else -1
