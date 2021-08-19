class Solution:
    def numPermsDISequence(self, S: str) -> int:
        n = len(S)
        mod = 10**9 + 7
        # solns[above][below]
        # if decreasing:
        # answer = sum solns[above+k][below-k-1]
        # if increasing:
        # answer = sum solns[above-k-1][below+k]

        solns = [[0] * (n + 2) for _ in range(n + 2)]
        solns[0][0] = 1
        for i in range(1, n + 1):
            for j in range(i + 1):
                k = i - j
                if S[-i] == 'D':
                    for r in range(0, k):
                        solns[j][k] += solns[j + r][k - r - 1]
                else:
                    for r in range(0, j):
                        solns[j][k] += solns[j - r - 1][k + r]
                solns[j][k] %= mod

        result = sum(solns[i][n - i] for i in range(n + 1))
        return result % mod
