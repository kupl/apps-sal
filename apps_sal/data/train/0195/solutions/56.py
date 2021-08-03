class Solution:
    def countTriplets(self, A: List[int]) -> int:

        # ans = 0
        n = len(A)

        @lru_cache(None)
        def dfs(i, pre):
            if i == 4 and not pre:
                return 1
            ans = 0
            for a in A:
                if (i > 1 and not pre & a) or (i == 1 and not a):
                    ans += n ** (3 - i)
                elif i < 3:
                    ans += dfs(i + 1, pre & a if i > 1 else a)
            return ans

        return dfs(1, None)
