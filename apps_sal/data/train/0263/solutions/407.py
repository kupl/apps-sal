class Solution:

    def knightDialer(self, n: int) -> int:
        moves = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 5: [], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [2, 4], 0: [4, 6]}
        dp1 = [1] * 10
        for i in range(n - 1):
            dp2 = [0] * 10
            for digit in range(10):
                for neib in moves[digit]:
                    dp2[digit] += dp1[neib]
                    dp2[digit] %= pow(10, 9) + 7
            dp1 = dp2
        return sum(dp1) % (pow(10, 9) + 7)
