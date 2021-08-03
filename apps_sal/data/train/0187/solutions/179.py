class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        # greedy: put the most people on at a given turn
        # why would you ever wait? I dont think you would, might as well take the instant profit
        # mostly because theres no reason to leave money on the table
        # when would you definitely not wait?

        remaining_customers = 0
        max_profit = 0
        profit = 0
        spin = 0
        best_spin = 0
        while remaining_customers > 0 or spin < len(customers):
            while spin < len(customers):

                remaining_customers += customers[spin]
                boarded = min(4, remaining_customers)
                remaining_customers -= boarded
                profit = profit + boardingCost * boarded - runningCost
                #print('Profit after spin {} is {}'.format(spin+1, profit))
                if profit > max_profit:
                    max_profit = profit
                    best_spin = spin
                spin += 1

            boarded = min(4, remaining_customers)
            remaining_customers -= boarded
            profit = profit + boardingCost * boarded - runningCost
            if profit > max_profit:
                max_profit = profit
                best_spin = spin
            spin += 1
            #print('Profit after spin {} is {}'.format(spin+1, profit))
        if max_profit <= 0:
            return -1
        else:
            return best_spin + 1
