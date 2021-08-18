class Solution:
    def minDifficulty(self, jD: List[int], d: int) -> int:
        if len(jD) < d:
            return -1
        memo = {}

        def dp(memo, jD, i, d):
            if len(jD) - i < d:
                return -1
            if d == 1:
                return max(jD[i:])
            if (i, d) in memo:
                return memo[(i, d)]
            ans, cur = 9999999999, 0
            for j in range(i, len(jD)):
                cur = max(cur, jD[j])
                x = dp(memo, jD, j + 1, d - 1)
                if x != -1:
                    ans = min(ans, cur + x)
            memo[(i, d)] = ans
            return ans
        return dp(memo, jD, 0, d)
