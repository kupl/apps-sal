class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:

        @lru_cache(None)
        def fun(last, no, con):
            if no == n:
                return 1
            count = 0
            for i in range(6):
                if i != last:
                    count += fun(i, no + 1, 1)
                elif con < rollMax[i]:
                    count += fun(i, no + 1, con + 1)
            return count
        ans = 0
        for i in range(6):
            ans += fun(i, 1, 1)
        return ans % (10 ** 9 + 7)
