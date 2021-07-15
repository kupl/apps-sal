class Solution:
    def dieSimulator(self, n0, rollMax):
        nfaces = len(rollMax)
        lst = [[0] * (nfaces + 1) for _ in range(n0 + 1)]
        lst[0][-1] = 1
        for n in range(1, n0 + 1):
            for face in range(nfaces):
                for i in range(n, -1, -1):
                    if n - rollMax[face] > i:
                        break
                    lst[n][face] += lst[i][-1] - lst[i][face]
            lst[n][-1] = sum(lst[n][:-1])
        return lst[-1][-1] % (10**9 + 7)
