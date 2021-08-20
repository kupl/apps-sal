class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:

        @lru_cache(maxsize=None)
        def _recursive(a):
            if a == 0:
                return 0
            min_n = 1000000000.0
            for c in coins:
                if c <= a:
                    sub_a = _recursive(a - c)
                    if sub_a != -1:
                        min_n = min(min_n, sub_a + 1)
            return min_n if min_n != 1000000000.0 else -1
        return _recursive(amount)
