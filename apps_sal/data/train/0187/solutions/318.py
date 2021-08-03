class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        totalCust = 0
        # for i in customers:
        #     totalCust += i
        # print(\"total cust \",totalCust)
        n = len(customers)
        ct = 0
        curr = 0
        profit = 0
        res = 0
        maxx = -999999
        pt = 0
        while True:
            ct += 1
            # print()
            if pt < n:
                totalCust += customers[pt]
                pt += 1
            if totalCust < 4:
                curr += totalCust
                totalCust = 0
                profit = curr * boardingCost - ct * runningCost
                if maxx < profit:
                    # print(\"dfffdfds\",res)
                    maxx = profit
                    res = ct
                # print(profit,ct)
                if pt == n:
                    break
                # break
            else:
                totalCust -= 4
                curr += 4
                profit = curr * boardingCost - ct * runningCost
                if maxx < profit:
                    # print(\"hhbbajskd\")
                    maxx = profit
                    res = ct
        if profit > 0:

            return res
        else:
            return -1
