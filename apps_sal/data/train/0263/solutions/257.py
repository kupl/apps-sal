class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        p = math.pow(10, 9) + 7
        c = {}
        c[1] = [6, 8]
        c[2] = [7, 9]
        c[3] = [4, 8]
        c[4] = [3, 9, 0]
        c[5] = []
        c[6] = [1, 7, 0]
        c[7] = [2, 6]
        c[8] = [1, 3]
        c[9] = [2, 4]
        c[0] = [4, 6]
        dp = [[None for _ in range(n + 1)]for _ in range(10)]
        for i in range(10):
            dp[i][1] = 1
            dp[i][2] = len(c[i])

        def find(i, x):
            if dp[i][x] is not None:
                return dp[i][x]
            dp[i][x] = 0
            for j in c[i]:
                dp[i][x] += find(j, x - 1) % p
            return dp[i][x]
        res = 0
        for i in range(10):
            res += find(i, n) % p
        return int(res % p)
