class Solution:
    def knightDialer(self, n: int) -> int:
        jump = {
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [1, 7, 0],
            7: [6, 2],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6]
        }

        dp = [1] * 10
        for _ in range(n - 1):
            newDp = [1] * 10
            for i in range(10):
                res = 0
                for item in jump[i]:
                    res += dp[item]
                res %= 1000000007
                newDp[i] = res
            dp = newDp
        return sum(dp) % 1000000007
