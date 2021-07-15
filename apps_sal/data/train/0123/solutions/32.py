class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        '''
         construct a 2d dp[i][j] where i is i different songs and
         j is the length of the playlist, also track the remaining songs r:
         for dp update, we have two options:
         if i <= k:
            1. add a new song to the list, r -= 1
         else:
            if r > L-j
                1. add a new song to the list, r -= 1
                2. add an existing song
            else:
                1. add a new song
         ''' 
        @lru_cache(None)
        def dp(unique, total, r):
            if total == L:
                return 1
            if unique <= K:
                return r * dp(unique+1, total+1, r-1)
            else:
                ans = 0
                if r < L-total:
                    # add an existing song
                    ans += (unique-K) * dp(unique, total+1, r)
                # add a new song
                ans += r * dp(unique+1, total+1, r-1)
                return ans

        return dp(0, 0, N) % (10**9+7)
