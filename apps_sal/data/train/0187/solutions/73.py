class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if boardingCost * 4 - runningCost <= 0:
            return -1
        m_profit = profit = m_run = run = left = 0
        for i in range(len(customers)):
            customer = customers[i]
            if customer + left <= 4:
                if run <= i:
                    run += 1
                    profit += (customer + left) * boardingCost - runningCost
                    left = 0
                else:
                    left += customer
            else:
                r = (customer + left) // 4
                run += r
                profit += r * 4 * boardingCost - r * runningCost
                left = (customer + left) % 4
            if profit > m_profit:
                m_profit = profit
                m_run = run
        if left > 0:
            profit += left * boardingCost - runningCost
            run += 1
            if profit > m_profit:
                m_run = run
        if m_profit > 0:
            return m_run
        return -1
