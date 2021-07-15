class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        F = [[0 for i in range(6)] for i in range(n + 1)]
        sumF = [0 for i in range(n + 1)]
        for i in range(6):
            F[1][i] = 1
        sumF[0] = 6
        MOD = 10**9 + 7
        for i in range(2, n + 1):
            for j in range(6):
                for p in range(1, rollMax[j] + 1):
                    if i == p:
                        F[i][j] = (F[i][j] + 1) % MOD
                        continue
                    for k in range(6):
                        if j == k: continue
                        if i > p:
                            F[i][j] = (F[i][j] + F[i - p][k]) % MOD

        res = 0
        for i in range(6):
            res = (res + F[n][i]) % MOD
            # print(F[n][i])
        return round(res)
        
        #1(11), 2(11), 3(11), 4(11), 5(11), 6(11) -> 6
        #1(22), 2(22), 3(22), 4(22), 5(22), 6(22) -> 6
        #1(33), 2(33), 3(33), 4(33), 5(33), 6(33) -> 6
        #

