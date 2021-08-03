class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        restCustomers = 0

        ans = 0
        curRote = 0
        cur = 0
        customerIndex = 0
        while customerIndex < len(customers):
            restCustomers += customers[customerIndex]
            curRote += 1
            if cur < cur + boardingCost * min(restCustomers, 4) - runningCost:
                ans = curRote
            cur += boardingCost * min(restCustomers, 4) - runningCost
            restCustomers = max(restCustomers - 4, 0)
            customerIndex += 1

            while restCustomers >= 4:
                curRote += 1

                if cur < cur + boardingCost * min(restCustomers, 4) - runningCost:
                    ans = curRote

                cur += boardingCost * 4 - runningCost

                restCustomers = max(restCustomers - 4, 0)
                if customerIndex < len(customers):
                    restCustomers += customers[customerIndex]
                customerIndex += 1

        if cur < cur + boardingCost * restCustomers - runningCost:
            ans += 1

        if ans == 0:
            return -1
        return ans
