class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10**9 + 7
        memoi = {}
        def numbers(n, prev, prevCount):
            if n == 0: return 1
            if (n, prev, prevCount) in memoi: 
                return memoi[n, prev, prevCount]
            res = 0
            for face in range(1, 7):
                if face != prev or rollMax[face-1] > prevCount:
                    res = (res + numbers(n - 1, face, prevCount * (face == prev) + 1)) % MOD
            memoi[n, prev, prevCount] = res
            return res
        return numbers(n, -1, 0)

