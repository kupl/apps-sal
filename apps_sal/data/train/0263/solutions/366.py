class Solution:

    def knightDialer(self, n: int) -> int:
        memo = {}
        pos = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 5: [], 6: [1, 7, 0], 7: [2, 6], 8: [3, 1], 9: [2, 4], 0: [6, 4]}
        res = 0
        mod = 10 ** 9 + 7

        def recur(i, hops):
            if (i, hops) in memo:
                return memo[i, hops]
            if hops == 0:
                return 1
            cnt = 0
            for nums in pos[i]:
                cnt += recur(nums, hops - 1)
                memo[i, hops] = cnt
            return cnt
        for i in range(10):
            res += recur(i, n - 1)
        return res % mod
