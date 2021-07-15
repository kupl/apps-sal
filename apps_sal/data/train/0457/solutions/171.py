class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(maxsize=None)
        def _recursive(a):
            if a == 0:
                return 0
            min_n = 1e9
            for c in coins:
                if c <= a:
                    sub_a = _recursive(a - c)
                    if sub_a != -1:
                        min_n = min(min_n, sub_a + 1)
            return min_n if min_n != 1e9 else -1
        return _recursive(amount)
    
    # Button-up
    # def coinChange(self, coins: List[int], amount: int) -> int:
        # states = [0] * (amount + 1)
        # for s in range(0, amount+1):
        #     if s == 0:
        #         states[s] = 0
        #     else:
        #         min_n = 1e9
        #         for c in coins:
        #             if c <= s and states[s-c] != -1:
        #                 min_n = min(min_n, 1 + states[s-c])
        #         if min_n == 1e9:
        #             states[s] = -1
        #         else:
        #             states[s] = min_n
        # return states[amount]

