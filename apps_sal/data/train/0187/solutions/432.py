class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        arr = []
        remain = 0
        for customer in customers:
            remain += customer
            (remain, cust) = (max(0, remain - 4), min(remain, 4))
            arr.append(cust)
        while remain > 0:
            arr.append(min(4, remain))
            remain -= 4
        pro = 0
        res = 0
        for cust in arr[::-1]:
            pro += cust * boardingCost
            pro -= runningCost
            res += 1
            if pro <= 0:
                res = 0
            pro = max(pro, 0)
        return res if res else -1
