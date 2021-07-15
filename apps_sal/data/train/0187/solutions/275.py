class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        i = 0
        max_profit = -1
        turn = 0
        cur_profit = 0
        remain = 0
        while i < len(customers) or remain:
            remain += customers[i] if i < len(customers) else 0
            board = min(remain, 4)
            remain -= board
            cur_profit += board * boardingCost - runningCost
            # max_profit = max(max_profit, cur_profit)
            if max_profit < cur_profit:
                max_profit = cur_profit
                turn = i + 1
            i += 1
        return turn if max_profit > 0 else -1
