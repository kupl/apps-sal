class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if not customers:
            return -1

        profit = 0
        steps = 0
        waiting_customers = 0
        arrived_customers = customers[0]
        on_board = 0
        step = 1
        while arrived_customers != -1 or waiting_customers:
            if arrived_customers == -1:
                arrived_customers = 0
            if waiting_customers > 4:
                on_board += 4
                waiting_customers += arrived_customers - 4
            else:
                vacant_seats = 4 - waiting_customers
                on_board += waiting_customers
                waiting_customers = 0
                if arrived_customers >= vacant_seats:
                    on_board += vacant_seats
                    arrived_customers -= vacant_seats
                else:
                    on_board += arrived_customers
                    arrived_customers = 0
                waiting_customers += arrived_customers

            # print('on board = {}, waiting = {}'.format(on_board, waiting_customers))
            if boardingCost * on_board - step * runningCost > profit:
                steps = step
                profit = boardingCost * on_board - step * runningCost

            step += 1

            try:
                arrived_customers = customers[step - 1]
            except IndexError:
                arrived_customers = -1

        if profit <= 0:
            return -1

        return steps
