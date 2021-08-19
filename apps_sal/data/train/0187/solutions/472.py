class Solution:
    def minOperationsMaxProfit(self, customers: List[int], bc: int, rc: int) -> int:
        profit = 0
        r = 0
        cnt = 0
        max_prof = 0
        ans = -1
        for c in customers:
            r += c
            cnt += 1
            profit += (min(4, r) * bc - rc)
            # print(profit)
            if profit > max_prof:
                ans = cnt
                max_prof = profit
            r = max(0, r - 4)

        times = int(r / 4)
        cnt += times
        profit += (r * bc - times * rc)
        if profit > max_prof:
            max_prof = profit
            ans = cnt

        if r % 4 > 0:
            profit += ((r % 4) * bc - rc)
            cnt += 1
            if profit > max_prof:
                max_prof = profit
                ans = cnt

        return ans
