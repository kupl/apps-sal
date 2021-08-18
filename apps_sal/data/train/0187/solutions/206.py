class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        max_amt, curr_amt, min_turns, curr_turns = 0, 0, 0, 0
        total, idx = 0, 0
        while (len(customers) > idx) or total > 0:
            if len(customers) > idx:
                total += customers[idx]
            idx += 1
            curr_turns += 1
            if total >= 4:
                curr = 4
            else:
                curr = total
            total -= curr
            curr_amt += (boardingCost * curr) - (runningCost)
            if curr_amt > max_amt:
                max_amt = curr_amt
                min_turns = curr_turns
        if not min_turns:
            return -1
        else:
            return min_turns
