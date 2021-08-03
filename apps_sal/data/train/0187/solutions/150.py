class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:

        max_profit = -sys.maxsize
        result = - sys.maxsize
        pending = 0
        running_counter = 0
        current_onboarding = 0
        for customer in customers:
            pending += customer
            running_counter += 1
            if pending > 0:
                real_boarding = min(4, pending)
                current_onboarding += real_boarding
                profit = current_onboarding * boardingCost - running_counter * runningCost

                if max_profit < profit:
                    max_profit = profit
                    result = running_counter
                    pass
                pending -= real_boarding
                pass
            pass

        while pending:
            running_counter += 1
            real_boarding = min(4, pending)
            current_onboarding += real_boarding
            pending -= real_boarding
            profit = current_onboarding * boardingCost - running_counter * runningCost

            if max_profit < profit:
                max_profit = profit
                result = running_counter
                pass
            pass

        if max_profit <= 0:
            return -1
        return result
