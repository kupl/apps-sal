class Solution:

    def minOperationsMaxProfit(self, customers: List[int], B: int, R: int) -> int:
        turns = 0
        boarded = 0
        max_profit = -1
        rem = 0
        max_turns = -1
        for (i, c) in enumerate(customers):
            (t, rem) = divmod(c + rem, 4)
            turns += t
            boarded += t * 4
            if turns <= i:
                turns += 1
                boarded += rem
                rem = 0
            profit = boarded * B - turns * R
            if profit > max_profit:
                max_profit = profit
                max_turns = turns
        if rem > 0:
            boarded += rem
            turns += 1
            profit = boarded * B - turns * R
            if profit > max_profit:
                max_profit = profit
                max_turns = turns
        return max_turns if max_profit > 0 else -1
