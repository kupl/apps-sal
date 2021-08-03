class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        ans = [0]
        remain = customers[0]
        idx = 1
        profit = 0
        current = 0
        while idx < len(customers) or remain != 0:
            up = min(4, remain)
            profit += up * boardingCost - runningCost
            if idx < len(customers):
                remain += customers[idx]
            remain -= up
            idx += 1
            ans.append(profit)
        ret = max(ans)
        return -1 if ret <= 0 else ans.index(ret)
