class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        q = 0
        profit = 0
        num_spins = 0
        num_customers = 0
        min_spins = float('inf')
        max_profit = -float('inf')
        be = runningCost // boardingCost
        if be >= 4:
            return -1
        for new_customers in customers:
            num_spins += 1
            q += new_customers
            loaded_customers = min(q, 4)
            q -= loaded_customers
            num_customers += loaded_customers
            profit = num_customers * boardingCost - num_spins * runningCost
            if profit > max_profit:
                max_profit = profit
                min_spins = num_spins
        if q:
            (full, partial) = divmod(q, 4)
            num_spins += full
            num_customers += 4 * full
            if partial > be:
                num_spins += 1
                num_customers += partial
            profit = num_customers * boardingCost - num_spins * runningCost
            if profit > max_profit:
                min_spins = num_spins
        return min_spins
