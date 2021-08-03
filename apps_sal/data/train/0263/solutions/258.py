class Solution:
    def knightDialer(self, N: int) -> int:
        numpad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
        dp = [1] * 10
        square = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [7, 0, 1], [2, 6], [1, 3], [2, 4]]
        mod = 10**9 + 7
        for i in range(2, N + 1):
            temp = [0] * 10
            for num in range(10):
                for j in square[num]:
                    temp[num] += dp[j] % mod
            dp = temp
        return sum(dp) % mod
