class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        k = {}
        mod = 10 ** 9 + 7
        for i in range(6):
            k[i] = [0 for i in range(rollMax[i])]
            if k[i]:
                k[i][-1] = 1
        for i in range(n):
            su = 0
            temp_su = [0 for j in range(6)]
            for j in range(6):
                val = sum(k[j])
                su += val
                temp_su[j] = val
            for j in range(6):
                temp = [x for x in k[j]]
                for x in range(rollMax[j] - 1):
                    temp[x] = k[j][x + 1] % mod
                temp[-1] = su - temp_su[j] % mod
                k[j] = temp
        return su % mod
