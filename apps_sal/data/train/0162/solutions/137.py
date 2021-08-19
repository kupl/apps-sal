class Solution:
    # 定义dp(i, j)是tex1中以i开头的和text2中以j开头的最长common subsequence
    # time O(mn) space O(mn)
    # 一般这种两个string/array让你dp的，都是定义以i/j为起点/终点的个数/长度
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0

        n, m = len(text1), len(text2)
        M = {}
        ret = 0
        # 和longest palindromic subsequence的dp状态转移一样

        def dp(i, j):
            if i >= n or j >= m:
                return 0

            if (i, j) in M:
                return M[(i, j)]

            M[(i, j)] = 0
            if text1[i] == text2[j]:
                M[(i, j)] = 1 + dp(i + 1, j + 1)
            else:
                M[(i, j)] = max(dp(i + 1, j), dp(i, j + 1))

            return M[(i, j)]

        return dp(0, 0)
