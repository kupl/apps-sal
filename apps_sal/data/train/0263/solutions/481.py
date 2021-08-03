class Solution:

    adjacency = {
        0: {4, 6},
        1: {8, 6},
        2: {7, 9},
        3: {8, 4},
        4: {3, 9, 0},
        5: {},
        6: {1, 7, 0},
        7: {2, 6},
        8: {1, 3},
        9: {2, 4}
    }

    def matrixExponentiation(self, a: List[List[int]], k: int) -> List[List[int]]:
        if k == 0:
            return [[1 if r == c else 0 for c in range(len(a[0]))] for r in range(len(a))]

        result = self.matrixExponentiation(a, k // 2)
        result = self.matrixMultiplication(result, result)

        if k % 2 == 1:
            result = self.matrixMultiplication(a, result)

        return result

    def matrixMultiplication(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        m, n, p = len(a), len(a[0]), len(b[0])
        assert len(a[0]) == len(b)

        matrix = [[0] * p for _ in range(m)]

        for r in range(m):
            for c in range(p):
                for i in range(n):
                    matrix[r][c] += a[r][i] * b[i][c]

        return matrix

    def knightDialer(self, n: int):
        matrix = [[(1 if r in Solution.adjacency[c] else 0) for c in range(10)] for r in range(10)]
        matrix = self.matrixExponentiation(matrix, n - 1)

        count = [[1] for _ in range(10)]
        count = self.matrixMultiplication(matrix, count)

        return sum((sum(r) for r in count)) % (10 ** 9 + 7)

    def knightDialerDP(self, n: int):
        count = [1 for _ in range(10)]

        for _ in range(n - 1):
            count = [sum(count[next_digit] for next_digit in Solution.adjacency[digit]) for digit in range(10)]

        return sum(count) % (10 ** 9 + 7)
