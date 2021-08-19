from functools import lru_cache


class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        @lru_cache(maxsize=None)
        def helper(p1, p2) -> int:
            if p1 == len(text1) or p2 == len(text2):
                return 0
            option1 = dp[p1 + 1][p2] if visited[p1 + 1][p2] == 1 else helper(p1 + 1, p2)
            first_occurrence = text2.find(text1[p1], p2)
            if first_occurrence != -1:
                option2 = dp[p1 + 1][first_occurrence + 1] + 1 if visited[p1 + 1][first_occurrence + 1] == 1 else 1 + helper(p1 + 1, first_occurrence + 1)
            else:
                option2 = 0
            visited[p1][p2] = 1
            dp[p1][p2] = max(option1, option2)
            return dp[p1][p2]
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        visited = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        return helper(0, 0)
