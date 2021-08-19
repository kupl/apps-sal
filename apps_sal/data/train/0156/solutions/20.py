from functools import lru_cache


class Solution:

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        (m, n) = (len(str1), len(str2))

        @lru_cache(None)
        def dfs(i1, i2):
            if i1 == m or i2 == n:
                return ''
            if str1[i1] == str2[i2]:
                return str1[i1] + dfs(i1 + 1, i2 + 1)
            (x, y) = (dfs(i1 + 1, i2), dfs(i1, i2 + 1))
            if len(x) > len(y):
                return x
            else:
                return y
        res = dfs(0, 0)
        (ans, idx1, idx2) = ('', 0, 0)
        for c in res:
            while idx1 < m and str1[idx1] != c:
                ans += str1[idx1]
                idx1 += 1
            while idx2 < n and str2[idx2] != c:
                ans += str2[idx2]
                idx2 += 1
            ans += c
            idx1 += 1
            idx2 += 1
        ans += str1[idx1:]
        ans += str2[idx2:]
        return ans
