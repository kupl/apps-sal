class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        left = 0
        required = 0
        for cus in customers:
            required += 1
            left += cus
            left -= min(left, 4)
        maxRot = required + ceil(left / 4)
        m_ = {0: -1}
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
            maxP = max(maxP, profit)
            if profit not in m_:
                m_[profit] = rotCnt + 1
            rotCnt += 1
        return m_[maxP]
