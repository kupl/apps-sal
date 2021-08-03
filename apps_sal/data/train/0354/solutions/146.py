from functools import lru_cache


class Solution:

    @staticmethod
    def ans_mod(n):
        return n % (10**9 + 7)

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        # so we need to think about

        @lru_cache(None)
        def roll(val, consec_rolls, rolls_left):
            if rolls_left == 0:
                return 1

            ans = 0

            if consec_rolls < rollMax[val]:
                ans += roll(val, consec_rolls + 1, rolls_left - 1)

            # now we consider all other possible rolls but not the same val
            for i in range(6):
                if i == val:
                    continue
                ans += roll(i, 1, rolls_left - 1)
            return ans

        return self.ans_mod(roll(0, 0, n))
