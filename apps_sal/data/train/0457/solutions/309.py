class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        matrix = [[0 for i in range(amount + 1)] for j in range(len(coins) + 1)]

        for i in range(len(matrix)):
            matrix[i][0] = 0
        for i in range(1, amount + 1):
            matrix[0][i] = sys.maxsize

        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if j < coins[i - 1]:
                    matrix[i][j] = matrix[i - 1][j]
                else:
                    matrix[i][j] = min(matrix[i - 1][j], 1 + matrix[i][j - coins[i - 1]])
        #print (matrix)
        if matrix[-1][-1] == sys.maxsize:
            return -1
        return matrix[-1][-1]
