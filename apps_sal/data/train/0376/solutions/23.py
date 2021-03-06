def tri_score(a1, a2, a3):
    return a1 * a2 * a3


class Solution:

    def __init__(self):
        self.memory = []

    def minScoreTriangulation(self, A) -> int:
        n = len(A)
        self.memory = [[None for _ in range(j + 1)] for j in range(n)]
        return self.minScoreTriangulationPart(A, 0, len(A) - 1)

    def minScoreTriangulationPart(self, A, start: int, end: int) -> int:
        if end - start < 2:
            return 0
        elif self.memory[end][start]:
            return self.memory[end][start]
        elif end - start == 2:
            res = tri_score(A[start], A[start + 1], A[start + 2])
            self.memory[end][start] = res
            return res
        res = min((tri_score(A[start], A[end], A[k]) + self.minScoreTriangulationPart(A, start, k) + self.minScoreTriangulationPart(A, k, end) for k in range(start + 1, end)))
        self.memory[end][start] = res
        return res
