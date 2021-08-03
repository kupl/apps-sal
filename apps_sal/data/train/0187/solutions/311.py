class Solution:
    def minOperationsMaxProfit(self, cust: List[int], bc: int, rc: int) -> int:
        cust.reverse()
        wait, profit, t, max_p, ans = 0, 0, 0, float('-inf'), 0
        while cust or wait:
            if cust:
                wait += cust.pop()
            if wait >= 4:
                profit += 4 * bc
            else:
                profit += wait * bc
            wait = max(0, wait - 4)
            profit -= rc
            t += 1
            if profit > max_p:
                ans = t
                max_p = profit
        return ans if max_p > 0 else -1
