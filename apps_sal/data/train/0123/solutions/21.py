class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        cache = {}
        def dp(i, j):
            if i == 0:
                return +(j == 0)
            if (i,j) in cache:
                return cache[(i,j)]
            ans = dp(i-1, j-1) * (N-j+1)
            ans += dp(i-1, j) * max(j-K, 0)
            ans %= (10**9+7)
            cache[(i,j)] = ans
            return ans

        return dp(L, N)
