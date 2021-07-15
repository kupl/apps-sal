class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        
        dp = {}
        MOD = 10**9 + 7
        
        def moveOnce(i0, steps0):
            if steps0 == 0:
                if i0 == 0:
                    return 1
                return 0
            
            if (i0, steps0) in dp:
                return dp[(i0, steps0)]
            if i0 > steps0:
                ans = 0
            else:
                if i0 == 0:
                    ans = moveOnce(i0+1, steps0-1) + moveOnce(i0, steps0-1)
                elif i0 == arrLen-1:
                    ans = moveOnce(i0-1, steps0-1) + moveOnce(i0, steps0-1)
                else:
                    ans = moveOnce(i0+1, steps0-1) + moveOnce(i0-1, steps0-1) + moveOnce(i0, steps0-1)
            dp[(i0, steps0)] = ans % MOD
            return dp[(i0, steps0)]
        
        return moveOnce(0, steps)
