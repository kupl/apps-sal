class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        mod = 10**9 + 7
        memo = {}

        def helper(i, j):
            nonlocal N, K
            if i == 0:
                if j == 0:
                    return 1
                else:
                    return 0
            if (i, j) in memo:
                return memo[(i, j)]
            ans = 0
            ans += helper(i - 1, j - 1) * (N - (j - 1))
            ans += helper(i - 1, j) * max(0, j - K)
            memo[(i, j)] = ans % mod
            return ans % mod
        return helper(L, N)
