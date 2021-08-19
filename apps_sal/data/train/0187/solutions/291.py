class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if 4 * boardingCost <= runningCost:
            return -1
        wait = 0
        n = len(customers)
        pro = 0
        max_pro = 0
        ans = 0
        i = 0
        while i < n or wait != 0:
            c = customers[i] if i < n else 0
            take = min(wait + c, 4)
            wait += c - take
            pro += take * boardingCost - runningCost
            i += 1
            if pro > max_pro:
                max_pro = max(max_pro, pro)
                ans = i
        return ans
