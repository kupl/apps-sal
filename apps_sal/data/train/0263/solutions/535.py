class Solution:

    def knightDialer(self, n: int) -> int:
        num = 0
        stack = [(1, i, i) for i in range(10)]
        pos = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4], 0: [4, 6]}
        memo = [[1] * 10 for _ in range(n)]
        for i in range(1, n):
            memo[i][0] = memo[i - 1][4] + memo[i - 1][6]
            memo[i][1] = memo[i - 1][6] + memo[i - 1][8]
            memo[i][2] = memo[i - 1][7] + memo[i - 1][9]
            memo[i][3] = memo[i - 1][4] + memo[i - 1][8]
            memo[i][4] = memo[i - 1][0] + memo[i - 1][3] + memo[i - 1][9]
            memo[i][5] = 0
            memo[i][6] = memo[i - 1][1] + memo[i - 1][7] + memo[i - 1][0]
            memo[i][7] = memo[i - 1][2] + memo[i - 1][6]
            memo[i][8] = memo[i - 1][1] + memo[i - 1][3]
            memo[i][9] = memo[i - 1][2] + memo[i - 1][4]
        return sum(memo[-1]) % (10 ** 9 + 7)
