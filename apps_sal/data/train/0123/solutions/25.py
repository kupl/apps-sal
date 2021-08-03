class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        mod = 10**9 + 7
        memo = {}
        # helper(i,j) returns the number of playlists of len i
        # that have exactly j unique songs

        def helper(i, j):
            nonlocal N, K
            if i == 0:
                if j == 0:
                    # base case
                    # helper(0,0) returns 1
                    return 1
                else:
                    return 0
            if (i, j) in memo:
                return memo[(i, j)]
            ans = 0
            # the jth song is unique,
            # then the jth song has (N-(j-1)) possibilities
            ans += helper(i - 1, j - 1) * (N - (j - 1))
            # the jth song is not unique
            # it is the same as one of the previous songs
            # then the jth song has max(0, j-K) possibilities
            # since it can be the same as the previous K songs
            ans += helper(i - 1, j) * max(0, j - K)
            memo[(i, j)] = ans % mod
            return ans % mod
        return helper(L, N)
