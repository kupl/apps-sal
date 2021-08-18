class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        D = []
        for i in range(1001):
            D.append([0] * 1002)
        best = 0
        for second in range(len(A) - 1, -1, -1):
            for first in range(second - 1, -1, -1):
                diff = A[second] - A[first]
                if diff < 0:
                    diff = 500 + -1 * diff
                D[first][diff] = D[second][diff] + 1
                if D[first][diff] > best:
                    best = D[first][diff]
        return best + 1
