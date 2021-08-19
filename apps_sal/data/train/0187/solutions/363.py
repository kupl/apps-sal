class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        left = 0
        required = 0
        for cus in customers:
            required += 1
            left += cus
            left -= min(left, 4)
        maxRot = required + ceil(left / 4)
        (mP, mR) = (0, -1)
        rotCnt = 0
        c = 0
        profit = 0
        maxP = 0
        while rotCnt < maxRot:
            if rotCnt < len(customers):
                c += customers[rotCnt]
            roundP = min(c, 4) * boardingCost
            c -= min(c, 4)
            roundP -= runningCost
            profit += roundP
            if profit > mP:
                mR = rotCnt + 1
                mP = profit
            rotCnt += 1
        return mR
