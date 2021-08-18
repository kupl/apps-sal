
class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:

        slicesN = len(slices)
        target = slicesN // 3

        table1 = [[0 for i in range(slicesN)] for ti in range(target + 1)]
        table2 = [[0 for i in range(slicesN)] for ti in range(target + 1)]

        for ti in range(1, target + 1):
            for i in range(1, slicesN):
                if i == 1:
                    table1[ti][i] = slices[i]
                    table2[ti][i] = slices[i - 1]
                    continue
                table1[ti][i] = max(table1[ti][i - 1], table1[ti - 1][i - 2] + slices[i])
                table2[ti][i] = max(table2[ti][i - 1], table2[ti - 1][i - 2] + slices[i - 1])

        return max(table1[-1][-1], table2[-1][-1])
