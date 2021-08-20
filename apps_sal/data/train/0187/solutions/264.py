class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        boarded = carry = rotations = max_profit = 0
        ans = -1
        for (i, nc) in enumerate(customers):
            nc += carry
            boarded += min(4, nc)
            carry = max(0, nc - 4)
            if nc > 0:
                rotations += 1
            if rotations < i + 1:
                rotations = i + 1
            profit = boarded * boardingCost - rotations * runningCost
            if profit > max_profit:
                max_profit = profit
                ans = rotations
        while carry > 0:
            boarded += min(4, carry)
            carry = max(0, carry - 4)
            rotations += 1
            profit = boarded * boardingCost - rotations * runningCost
            if profit > max_profit:
                max_profit = profit
                ans = rotations
        return ans
