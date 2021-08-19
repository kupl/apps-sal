class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        modulo = 10 ** 9 + 7
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


"\nclass Solution:\n    def numRollsToTarget(self, d: int, f: int, target: int) -> int:\n        modulo = 10**9 + 7\n        #don't use row 0 and all column 0 \n        dp = [[0 for i in range(target+1)] for j in range(d+1)]\n        \n        #from die No. 1 to d\n        for dd in range(1, d+1):\n            #for target from 0 to min(f*dd, target)\n            for tt in range(dd, min(f * dd, target) + 1 ):\n                if dd == 1:\n                    dp[dd][tt] = 1\n                else:\n                    end   = tt - 1\n                    start = max(1, tt - f)\n                    dp[dd][tt] = sum(dp[dd-1][start:end+1])\n    \n        return dp[d][target] % modulo                          \n        \n  \n        #f(d, target) = f(d-1, target-1) + f(d-1, target-2) + ... + f(d-1, target-f)  assuming target > f\n        modulo = 10**9 + 7\n        cache = {}\n        def numRollsToTargetHelper(dd, tt):\n            if cache.get((dd,tt)) != None:\n                return cache[(dd,tt)]\n            nonlocal f\n            if dd == 1:\n                if tt <= f:\n                    return 1\n                else:\n                    return 0\n            \n            ret = 0\n            for i in range(1, f+1):\n                if tt - i > 0:\n                    ret += numRollsToTargetHelper(dd-1, tt-i)\n            cache[(dd,tt)] = ret\n            return ret\n        \n        ret = numRollsToTargetHelper(d, target)\n        return ret % modulo\n        "
