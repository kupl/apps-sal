class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        def cost(st, i, j):
            res = 0
            while j > i:
                if st[i] != st[j]:
                    res += 1
                i += 1
                j -= 1
            return res
        memo = {}

        def dfs(l, r, k):
            if r - l < k:
                return float('inf')
            if r - l == k:
                return 0
            if k == 1:
                return cost(s, l, r - 1)
            if (l, r, k) in memo:
                return memo[l, r, k]
            memo[l, r, k] = float('inf')
            for i in range(l + 1, r):
                memo[l, r, k] = min(memo[l, r, k], dfs(l, i, k - 1) + cost(s, i, r - 1))
            return memo[l, r, k]
        return dfs(0, len(s), k)
