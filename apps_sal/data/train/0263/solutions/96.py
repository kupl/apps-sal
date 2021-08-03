class Solution:
    def knightDialer(self, n: int) -> int:
        prev = [0] * 10
        dp = [1] * 10

        m = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }

        def parents(x):
            return m[x]

        for l in range(1, n + 1):
            for x in range(10):
                for prevX in parents(x):
                    dp[x] += prev[prevX]
                    dp[x] = dp[x] % (10 ** 9 + 7)
            prev, dp = dp, [0] * 10

        return sum(prev) % (10 ** 9 + 7)
