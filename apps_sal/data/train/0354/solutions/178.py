class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10**9+7
        dp = {}
        
        def helper(preV, repeat, n0):
            if n0 == 0:
                return 1
            if (preV, repeat, n0) in dp:
                return dp[(preV, repeat, n0)]
            
            subAns = 0
            for nextV in range(1, 7):
                if nextV == preV:
                    if repeat < rollMax[preV-1]:
                        subAns += helper(preV, repeat+1, n0-1)
                else:
                    subAns += helper(nextV, 1, n0-1)
            dp[(preV, repeat, n0)] = subAns % MOD
            return dp[(preV, repeat, n0)]
        return helper(-1, 0, n)
