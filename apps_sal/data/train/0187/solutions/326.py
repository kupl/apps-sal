class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        # max profit, rotating count
        max_tuple = (0, -1)

        profit = 0
        awaiting = 0
        turn = 0
        while awaiting > 0 or turn == 0 or turn < len(customers):
            if turn < len(customers):
                awaiting += customers[turn]
            count_pay = min(4, awaiting)
            awaiting -= count_pay

            profit += count_pay * boardingCost - runningCost
            # print(profit)
            if profit > max_tuple[0]:
                max_tuple = (profit, turn + 1)

            turn += 1

        return max_tuple[1]
