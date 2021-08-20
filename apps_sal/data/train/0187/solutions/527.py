class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if not customers:
            return -1
        profit = 4 * boardingCost - runningCost
        if profit <= 0:
            return -1
        cumulate = sum(customers)
        cum = 0
        rt = 0
        al = 0
        maxl = 0
        for item in customers:
            cum += item
            if cum >= 4:
                cum -= 4
                rt += 1
                al += 4
                maxl = max(maxl, al * boardingCost - rt * runningCost)
            else:
                rt += 1
                al += cum
                maxl = al * boardingCost - rt * runningCost
                cum = 0
        a = cum // 4
        b = cum % 4
        profit = boardingCost * b - runningCost
        if profit > 0:
            rt = rt + a + 1
        else:
            rt += a
        return rt
