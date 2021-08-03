class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        @lru_cache(None)
        def unique(length, uni):
            if uni == 0:
                return 0
            if length == 1:
                if uni == 1:
                    return N
                else:
                    return 0

            ret = unique(length - 1, uni - 1) * (N - uni + 1)
            ret += unique(length - 1, uni) * max(0, uni - K)

            return ret % (10**9 + 7)

        return unique(L, N)
