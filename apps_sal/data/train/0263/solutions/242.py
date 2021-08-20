class Solution:

    def knightDialer(self, N: int) -> int:
        d = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [4, 2], 5: [], 0: [4, 6]}

        @lru_cache(None)
        def helper(k, i):
            if k == 0:
                return 1
            r = 0
            for n in d[i]:
                r += helper(k - 1, n)
            return r
        ans = 0
        for n in list(d.keys()):
            ans += helper(N - 1, n)
        return ans % (10 ** 9 + 7)
