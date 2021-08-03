class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        # select 1 -> max of selecting n-1 from 2, 3n-1
        # not select 1 -> max of selecting n from 2, 3n
        # a table to fill: (either selected or not)
        #  1, 2, 3, ... 3n # pos
        # 0  maxSum
        # 1
        # 2
        #
        # n
        # num selected
        N = len(slices) // 3
        dpOn = [[-1 for i in range(3 * N)] for j in range(N + 1)]
        dpOff = [[-1 for i in range(3 * N)] for j in range(N + 1)]

        # first 1 selected
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
        # first 1 not selected
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
