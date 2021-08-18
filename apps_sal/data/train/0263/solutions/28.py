class Solution:
    def knightDialer(self, n):
        dmap = [[4, 6], [8, 6], [7, 9], [8, 4], [3, 9, 0], [], [1, 7, 0], [2, 6], [1, 3], [2, 4], [4, 6]]
        mod_val = 10 ** 9 + 7
        ans = 0
        dp1 = [1] * 10
        dp2 = [0] * 10

        for _ in range(2, n + 1):
            for j in range(0, 10):
                tv = dmap[j]
                for t in tv:
                    dp2[j] += dp1[t] % mod_val
            dp1 = dp2[:]
            dp2 = [0] * 10
        ans = sum(dp1) % mod_val
        return ans
