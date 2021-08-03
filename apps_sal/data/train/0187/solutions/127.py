class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:

        n = len(customers)
        dp = []
        reserved = 0
        on_board = 0
        rotation = 0
        for i in range(n):
            if reserved != 0:
                if reserved >= 4:
                    on_board += 4
                    reserved += customers[i] - 4
                else:
                    new_customers = 4 - reserved
                    if customers[i] >= new_customers:
                        on_board += 4
                        reserved = customers[i] - new_customers
                    else:
                        on_board += reserved + customers[i]
                        reserved = 0
            else:
                if customers[i] >= 4:
                    on_board += 4
                    reserved += customers[i] - 4
                else:
                    on_board += customers[i]
            rotation += 1

            dp.append(on_board * boardingCost - rotation * runningCost)

        for i in range(reserved // 4 + 1):
            if reserved >= 4:
                on_board += 4
                reserved -= 4
            else:
                on_board += reserved
                reserved = 0
            rotation += 1
            dp.append(on_board * boardingCost - rotation * runningCost)

        maxi = max(dp)
        return dp.index(max(dp)) + 1 if maxi >= 0 else -1
