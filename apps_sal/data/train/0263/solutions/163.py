MOVES = [
    [4, 6],
    [6, 8],
    [7, 9],
    [4, 8],
    [3, 9, 0],
    [],
    [1, 7, 0],
    [2, 6],
    [1, 3],
    [2, 4],
]

modulus = 10**9 + 7


class Solution:
    def knightDialer(self, n: int) -> int:
        dp = [1] * 10
        dp2 = [0] * 10
        for _ in range(1, n):
            for digit in range(10):
                dp2[digit] = 0
                for next_digit in MOVES[digit]:
                    dp2[digit] += dp[next_digit]
                    dp2[digit] %= modulus
            dp2, dp = dp, dp2

        result = 0
        for ways in dp:
            result += ways
            result %= modulus

        return result
