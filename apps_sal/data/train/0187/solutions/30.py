class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        wait = 0
        onboard = 0
        total = 0
        count = 0
        max_count = 0
        max_total = 0
        for (ind, cust) in enumerate(customers):
            count += 1
            if cust + wait > 4:
                wait = cust + wait - 4
                onboard = 4
            else:
                wait = 0
                onboard = cust + wait
            total = total + onboard * boardingCost - runningCost
            if max_total < total:
                max_total = total
                max_count = count
        while wait > 0:
            count += 1
            if wait > 4:
                onboard = 4
                wait = wait - 4
            else:
                onboard = wait
                wait = 0
            total = total + onboard * boardingCost - runningCost
            if max_total < total:
                max_total = total
                max_count = count
        if max_total > 0:
            return max_count
        return -1
