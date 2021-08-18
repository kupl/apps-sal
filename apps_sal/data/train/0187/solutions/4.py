class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        left = 0
        cost = 0
        i = 0
        m_cost = 0
        m = -1
        for c in customers:
            left += c
            if left <= 4:
                cost += left * boardingCost - runningCost
                left = 0
            else:
                cost += 4 * boardingCost - runningCost
                left -= 4
            i += 1
            if cost > m_cost:
                m_cost = cost
                m = i
        while left:
            if left <= 4:
                cost += left * boardingCost - runningCost
                left = 0
            else:
                cost += 4 * boardingCost - runningCost
                left -= 4
            i += 1
            if cost > m_cost:
                m_cost = cost
                m = i
        return m
