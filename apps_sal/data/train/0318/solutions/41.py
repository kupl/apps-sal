class Solution:

    def maxSizeSlices(self, slices: List[int]) -> int:
        N = len(slices)

        @lru_cache(None)
        def rec(cur, taken, avoid_last):
            if taken * 3 > N:
                return -math.inf
            if cur >= N:
                return 0 if taken * 3 == N else -math.inf
            ans = rec(cur + 1, taken, avoid_last)
            if avoid_last and cur == N - 1:
                return ans
            ans = max(ans, rec(cur + 2, taken + 1, avoid_last | (cur == 0)) + slices[cur])
            return ans
        return rec(0, 0, False)
