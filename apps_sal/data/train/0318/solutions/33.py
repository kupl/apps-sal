class Solution:

    def maxSizeSlices(self, slices: List[int]) -> int:
        N = len(slices) // 3
        dpOn = [[-1 for i in range(3 * N)] for j in range(N + 1)]
        dpOff = [[-1 for i in range(3 * N)] for j in range(N + 1)]
        dpOn[1][0] = slices[0]
        for i in range(1, 3 * N):
            dpOff[0][i] = 0
        for i in range(1, 3 * N):
            for j in range(1, N + 1):
                dpOff[j][i] = max(dpOn[j][i - 1], dpOff[j][i - 1])
                if dpOff[j - 1][i - 1] == -1:
                    dpOn[j][i] = -1
                else:
                    dpOn[j][i] = dpOff[j - 1][i - 1] + slices[i]
        maxVal = dpOff[N][3 * N - 1]
        dpOn = [[-1 for i in range(3 * N)] for j in range(N + 1)]
        dpOff = [[-1 for i in range(3 * N)] for j in range(N + 1)]
        for i in range(0, 3 * N):
            dpOff[0][i] = 0
        for i in range(1, 3 * N):
            for j in range(1, N + 1):
                dpOff[j][i] = max(dpOn[j][i - 1], dpOff[j][i - 1])
                if dpOff[j - 1][i - 1] == -1:
                    dpOn[j][i] = -1
                else:
                    dpOn[j][i] = dpOff[j - 1][i - 1] + slices[i]
        maxVal = max(maxVal, dpOn[N][3 * N - 1], dpOff[N][3 * N - 1])
        return maxVal
