class Solution:

    def knightDialer(self, n: int) -> int:
        self.res = 0
        mapping = {1: [6, 8], 2: [9, 7], 3: [8, 4], 4: [3, 9, 0], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [2, 4], 0: [4, 6], 5: []}
        memo = {}

        def helper(n, rem):
            if (n, rem) in memo:
                return memo[n, rem]
            if rem == 0:
                return 1
            res = 0
            for nei in mapping[n]:
                res += helper(nei, rem - 1)
            memo[n, rem] = res
            return res
        res = 0
        for i in range(10):
            res += helper(i, n - 1)
        return res % (10 ** 9 + 7)
