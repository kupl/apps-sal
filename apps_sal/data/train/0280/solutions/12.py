class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        def count_char(a):
            n = len(a)
            b = a[::-1]
            return sum(a[i] != b[i] for i in range(n)) // 2
        n = len(s)
        d = {}
        for i in range(n):
            for j in range(i, n):
                d[(i, j)] = count_char(s[i:j + 1])
        @lru_cache(None)
        def dfs(i, j, l):
            if l == j - i + 1:
                return 0
            if l == 1:
                return d[(i, j)]
            res = float('inf')
            for m in range(i, j - l + 2):
                res = min(res, d[(i, m)] + dfs(m + 1, j, l - 1))
            return res
        return dfs(0, len(s) - 1, k)
