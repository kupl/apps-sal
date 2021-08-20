class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        maxx = 0
        rem = 0
        i = 0
        profit = 0
        count = 0
        while True:
            if i < len(customers):
                if customers[i] > 4:
                    if i + 1 < len(customers):
                        customers[i + 1] = customers[i + 1] + (customers[i] - 4)
                        customers[i] = 4
                    else:
                        customers.append(customers[i] - 4)
                        customers[i] = 4
                count = count + customers[i]
                profit = count * boardingCost - (i + 1) * runningCost
                if profit > maxx:
                    maxx = profit
                    rem = i + 1
                i = i + 1
            else:
                break
        if rem == 0:
            return -1
        return rem
