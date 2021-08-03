class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        profit = 0
        waiting = 0
        rotations = 0
        ans = -1
        for c in customers:
            waiting += c
            cap = 0
            if waiting >= 4:
                waiting -= 4
                cap += 4
            else:
                cap = waiting
                waiting = 0
            cur_profit = profit + (cap * boardingCost) - runningCost
            rotations += 1
            if cur_profit > profit:
                ans = rotations
            profit = cur_profit

        if waiting > 0:
            req_rotations = math.ceil(waiting / 4)
            ignore = waiting // 4
            possible_profit = (waiting * boardingCost) - (req_rotations * runningCost)
            full_only = ((waiting - (waiting % 4)) * boardingCost) - (ignore * runningCost)
            if possible_profit > full_only:
                additional = req_rotations
                if profit + possible_profit > profit:
                    ans = rotations + req_rotations
            else:
                additional = ignore
                if profit + full_only > profit:
                    ans = rotations + ignore
        return ans
