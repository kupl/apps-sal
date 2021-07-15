class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        res = -1
        max_income = 0
        cur_customer = 0
        cur_income = 0
        cnt = 0
        full_income = 4 * boardingCost - runningCost
        for c in customers:
            cur_customer += c
            if cur_customer > 4:
                cur_customer -= 4
                cur_income += full_income
            else:
                cur_income += cur_customer * boardingCost - runningCost 
                cur_customer = 0
            cnt += 1
            if cur_income > max_income:
                max_income = cur_income
                res = cnt

        if full_income > 0:
            cnt += cur_customer // 4
            cur_customer %= 4
            cur_income += cnt * full_income
            if cur_income > max_income:
                max_income = cur_income
                res = cnt
            cur_income += cur_customer * boardingCost - runningCost
            if cur_income > max_income:
                max_income = cur_income
                res = cnt + 1
        return res
