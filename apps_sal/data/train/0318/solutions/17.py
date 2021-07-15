class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        k = len(slices) // 3

        dp1 = [[0] * len(slices) for _ in range(k + 1)]
        dp2 = [[0] * len(slices) for _ in range(k + 1)]
        
        for i in range(1, k + 1):
            for j in range(1, len(slices)):
                if j == 1:
                    dp1[i][j] = slices[j - 1]
                    dp2[i][j] = slices[j]
                else:
                    dp1[i][j] = max(dp1[i - 1][j - 2] + slices[j - 1], dp1[i][j - 1])
                    dp2[i][j] = max(dp2[i - 1][j - 2] + slices[j], dp2[i][j - 1])
        return max(dp1[-1][-1], dp2[-1][-1])
