class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        max_prof = -math.inf
        idx = -1
        sofar = 0
        profit_sofar = 0
        i = 0
        while True:
            if i < len(customers):
                sofar += customers[i]
            if sofar == 0 and i >= len(customers):
                break
            num_onboard = min(4, sofar)
            sofar -= num_onboard
            profit_sofar += num_onboard * boardingCost - runningCost
            if profit_sofar > max_prof:
                max_prof = profit_sofar
                idx = i
            i += 1
        return idx + 1 if max_prof > 0 else -1
