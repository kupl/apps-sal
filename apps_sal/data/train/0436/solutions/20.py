class Solution:
    def minDays(self, n: int) -> int:
        @lru_cache(None)
        def eat(remaining, day):
            if remaining == 0:
                return day

            e_3 = eat(remaining - (2 * (remaining // 3)), day + 1) if remaining % 3 == 0 else eat(remaining - remaining % 3, day + remaining % 3)
            e_2 = eat(remaining - (remaining // 2), day + 1) if remaining % 2 == 0 else eat(remaining - 1, day + 1)

            return min(e_3, e_2)
        return eat(n, 0)
