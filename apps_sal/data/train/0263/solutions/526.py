class Solution:
    def knightDialer(self, l: int) -> int:
        dpTable = [1] * 10
        for _ in range(l - 1):
            newTable = [0] * 10
            for i in [0, 1, 2, 3, 4, 6, 7, 8, 9]:
                if i == 0:
                    ret = dpTable[4] + dpTable[6]
                elif i == 1:
                    ret = dpTable[6] + dpTable[8]
                elif i == 2:
                    ret = dpTable[7] + dpTable[9]
                elif i == 3:
                    ret = dpTable[4] + dpTable[8]
                elif i == 4:
                    ret = dpTable[3] + dpTable[9] + dpTable[0]
                elif i == 6:
                    ret = dpTable[1] + dpTable[7] + dpTable[0]
                elif i == 7:
                    ret = dpTable[2] + dpTable[6]
                elif i == 8:
                    ret = dpTable[1] + dpTable[3]
                elif i == 9:
                    ret = dpTable[2] + dpTable[4]
                newTable[i] = ret % 1000000007
            dpTable = newTable
        return sum(dpTable) % 1000000007
