class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        modulo = 10**9 + 7
        dp = [[0 for i in range(target + 1)] for j in range(d + 1)]
        for dd in range(1, d + 1):
            for tt in range(dd, min(target, dd * f) + 1):
                if dd == 1:
                    dp[dd][tt] = 1
                else:
                    start = max(tt - f, 1)
                    end = tt - 1
                    dp[dd][tt] = sum(dp[dd - 1][start:end + 1])

        return dp[d][target] % modulo


'''
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        modulo = 10**9 + 7
        dp = [[0 for i in range(target+1)] for j in range(d+1)]
        
        for dd in range(1, d+1):
            for tt in range(dd, min(f * dd, target) + 1 ):
                if dd == 1:
                    dp[dd][tt] = 1
                else:
                    end   = tt - 1
                    start = max(1, tt - f)
                    dp[dd][tt] = sum(dp[dd-1][start:end+1])
    
        return dp[d][target] % modulo                          
        
  
        modulo = 10**9 + 7
        cache = {}
        def numRollsToTargetHelper(dd, tt):
            if cache.get((dd,tt)) != None:
                return cache[(dd,tt)]
            nonlocal f
            if dd == 1:
                if tt <= f:
                    return 1
                else:
                    return 0
            
            ret = 0
            for i in range(1, f+1):
                if tt - i > 0:
                    ret += numRollsToTargetHelper(dd-1, tt-i)
            cache[(dd,tt)] = ret
            return ret
        
        ret = numRollsToTargetHelper(d, target)
        return ret % modulo
        '''
