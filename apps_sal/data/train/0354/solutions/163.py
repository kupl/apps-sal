class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10**9 + 7
        memoi = [[1] + ([0] * (limit - 1)) for limit in rollMax]
        for _ in range(1, n):
            sumVal = sum(map(sum, memoi)) % MOD
            newMemoi = []
            for face in range(1, 7):
                limits = []
                limits.append((sumVal - sum(memoi[face-1])) % MOD)
                for limit in range(1, rollMax[face-1]):
                    limits.append(memoi[face-1][limit-1])
                newMemoi.append(limits)
            memoi = newMemoi
        return sum(map(sum, memoi)) % MOD

