class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        current_profit = 0
        from collections import deque
        deq = deque(customers)
        curr_customers = 0
        #rev_list = reversed(customers)
        max_profit, count_spin = 0, 0
        count = 0
        while True:
            count += 1
            if deq:
                curr_customers += deq.popleft()
            if curr_customers == 0 and not deq:
                count -= 1
                break
            else:
                if curr_customers >= 4:
                    curr_customers -= 4
                    current_profit += boardingCost * 4 - runningCost
                else:
                    current_profit += boardingCost * curr_customers - runningCost
                    curr_customers = 0
            if max_profit < current_profit:
                max_profit = current_profit
                count_spin = count
        return count_spin if max_profit > 0 else -1
