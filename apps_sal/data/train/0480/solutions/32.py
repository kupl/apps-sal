class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        @lru_cache(None)
        def simulate(currIdx, stepsTaken):
            nonlocal arrLen
            nonlocal steps
            if stepsTaken == steps:
                if currIdx == 0:
                    return 1
                return 0
            
            ret = 0
            
            moves = [currIdx, currIdx - 1, currIdx + 1]
            for nextIdx in moves:
                if nextIdx >= 0 and nextIdx < arrLen:
                    ret += simulate(nextIdx, stepsTaken + 1)
                    
            return ret
        
        return simulate(0, 0) % (10 ** 9 + 7)

