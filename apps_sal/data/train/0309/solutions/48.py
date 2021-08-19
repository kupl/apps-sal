class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        # d subproblem
        # index, difference
        D = []
        for i in range(1001):
            D.append([0] * 1002)  # first 501 is pos, second 501 is neg difference
        best = 0
        for second in range(len(A) - 1, -1, -1):
            for first in range(second - 1, -1, -1):
                diff = A[second] - A[first]
                if diff < 0:
                    diff = 500 + -1 * diff
                D[first][diff] = D[second][diff] + 1
                if D[first][diff] > best:
                    best = D[first][diff]
                    # print(f'best: {best}, first: {first}, diff: {diff}')
        # print(D[0][501+5])
        return best + 1
