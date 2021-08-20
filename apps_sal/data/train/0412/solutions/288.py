class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        matrix = [[1 if 1 <= x <= f and y == 0 else 0 for x in range(target + 1)] for y in range(0, d)]
        for row in range(1, d):
            for (col, val) in enumerate(matrix[row]):
                matrix[row][col] = sum(matrix[row - 1][max(0, col - f):max(0, col)])
        return matrix[d - 1][target] % (10 ** 9 + 7)
