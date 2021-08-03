class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        n = len(slices)
        nPick = n // 3
        total = [[[0] * (n + 1) for _ in range(nPick + 1)] for __ in range(2)]
        total[1][1][1] = slices[0]

        for i in range(1, nPick + 1):
            for j in range(2, n + 1):
                total[0][i][j] = max(slices[j - 1] + total[0][i - 1][j - 2], total[0][i][j - 1])
                total[1][i][j] = max(slices[j - 1] + total[1][i - 1][j - 2], total[1][i][j - 1])

        return max(max(total[0][nPick]), max(total[1][nPick][:-1]))
