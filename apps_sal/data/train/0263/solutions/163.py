MOVES = [
    [4, 6],  # 0
    [6, 8],  # 1
    [7, 9],  # 2
    [4, 8],  # 3
    [3, 9, 0],  # 4
    [],  # 5
    [1, 7, 0],  # 6
    [2, 6],  # 7
    [1, 3],  # 8
    [2, 4],  # 9
]

modulus = 10**9 + 7


class Solution:
    def knightDialer(self, n: int) -> int:
        dp = [1] * 10  # dp[i] = number of ways to get to digit in n moves, for n = 1, 2, ...
        dp2 = [0] * 10  # second copy of dp2 to avoid mutating dp while iterating over it
        for _ in range(1, n):
            for digit in range(10):
                dp2[digit] = 0
                for next_digit in MOVES[digit]:
                    dp2[digit] += dp[next_digit]
                    dp2[digit] %= modulus
            dp2, dp = dp, dp2  # swap out current dp

        result = 0
        for ways in dp:
            result += ways
            result %= modulus

        return result
