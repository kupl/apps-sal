class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        dp = [-1] * len(s)
        return self.dfs(s, k, 0, dp)

    def dfs(self, s: str, k: int, start: int, dp: List[int]) -> int:
        if start == len(s):
            return 1
        if s[start] == '0':
            return 0
        if dp[start] != -1:
            return dp[start]

        res, num = 0, 0

        for i in range(start, len(s)):
            num = num * 10 + (ord(s[i]) - ord('0'))

            if num > k:
                break

            res += self.dfs(s, k, i + 1, dp)
            res %= 10**9 + 7

        dp[start] = res
        return res
