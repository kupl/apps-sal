class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boarding_cost: int, running_cost: int) -> int:
        max_profit = 0
        max_profit_rotations = -1
        rotations = 0
        current_profit = 0
        in_line = 0
        for customer in customers:
            in_line += customer
            current_profit += min(in_line, 4) * boarding_cost - running_cost 
            in_line = max(in_line - 4, 0)
            rotations += 1
            if current_profit > max_profit:
                max_profit = current_profit
                max_profit_rotations = rotations
        while in_line > 0:
            current_profit += min(in_line, 4) * boarding_cost - running_cost
            in_line = max(in_line - 4, 0)
            rotations += 1
            if current_profit > max_profit:
                max_profit = current_profit
                max_profit_rotations = rotations
        return max_profit_rotations
        
'''
Input: customers = [10,9,6], boardingCost = 6, runningCost = 4
Output: 7
Explanation:
1. 10 customers arrive, 4 board and 6 wait for the next gondola, the wheel rotates. Current profit is 4 * $6 - 1 * $4 = $20.
2. 9 customers arrive, 4 board and 11 wait (2 originally waiting, 9 newly waiting), the wheel rotates. Current profit is 8 * $6 - 2 * $4 = $40.
3. The final 6 customers arrive, 4 board and 13 wait, the wheel rotates. Current profit is 12 * $6 - 3 * $4 = $60.
4. 4 board and 9 wait, the wheel rotates. Current profit is 16 * $6 - 4 * $4 = $80.
5. 4 board and 5 wait, the wheel rotates. Current profit is 20 * $6 - 5 * $4 = $100.
6. 4 board and 1 waits, the wheel rotates. Current profit is 24 * $6 - 6 * $4 = $120.
7. 1 boards, the wheel rotates. Current profit is 25 * $6 - 7 * $4 = $122.
The highest profit was $122 after rotating the wheel 7 times.

10 - 4 - 24

'''
