class Solution:

    def superEggDrop(self, K: int, N: int) -> int:
        if N == 1:
            return 1
        eggSolutions = [[None for n in range(N + 1)] for k in range(K + 1)]
        for n in range(1, N + 1):
            eggSolutions[1][n] = n
        for k in range(1, K + 1):
            eggSolutions[k][1] = 1
            eggSolutions[k][2] = 2
        nextPVals = [i for i in range(N + 1)]
        for k in range(2, K + 1):
            pVals = nextPVals
            nextPVals = [None, None, 2]
            pIndex = 2
            for n in range(3, N + 1):
                p = pVals[pIndex]
                minDrops = 1 + max(eggSolutions[k - 1][p - 1], eggSolutions[k][n - p])
                eggSolutions[k][n] = minDrops
                if eggSolutions[k][n] > eggSolutions[k][n - 1]:
                    pIndex += 1
                    nextPVals.append(n)
        return eggSolutions[K][N]
