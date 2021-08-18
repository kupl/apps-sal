class Solution:
    def knightDialer(self, n: int) -> int:

        dp = {}

        def nextStep(k):
            if k == 1:
                return [6, 8]
            if k == 2:
                return [7, 9]
            if k == 3:
                return [4, 8]
            if k == 4:
                return [9, 3, 0]
            if k == 6:
                return [7, 1, 0]
            if k == 7:
                return [6, 2]
            if k == 8:
                return [1, 3]
            if k == 9:
                return [4, 2]
            if k == 0:
                return [4, 6]

        def dfs(k, step):
            if k == 5 and step > 1:
                return 0
            if step == 1:
                return 1
            key = (k, step)
            if key in dp:
                return dp[key]
            dp[key] = sum([dfs(e, step - 1) for e in nextStep(k)])
            return dp[key]
        res = 0
        for i in range(10):
            res += dfs(i, n)
        return res % (10**9 + 7)
