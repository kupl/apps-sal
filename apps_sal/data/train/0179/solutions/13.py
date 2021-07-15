class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        dp = {}
        def dfs(i, t, prev, last):
            if t == -1:
                return float('inf')
            if i == len(s):
                return 0
            if (i, t, prev, last) in dp:
                return dp[(i, t, prev, last)]
            if s[i] == last:
                increase = 0
                if prev == 1 or prev == 9 or prev == 99:
                    increase = 1
                dp[(i, t, prev, last)] = increase + dfs(i + 1, t, prev + 1, last)
            else:
                take = dfs(i + 1, t, 1, s[i]) + 1
                remove = dfs(i + 1, t - 1, prev, last)
                dp[(i, t, prev, last)] = min(take, remove)
            return dp[(i, t, prev, last)]
        return dfs(0, k, 0, '')

