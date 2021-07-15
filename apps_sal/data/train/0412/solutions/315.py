class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if d <= target <= d*f:
            mod = 10**9 + 7
            def rec(d, f, t):
                
                if d == 1:
                    return 1 if 0 < t <= f else 0
                elif (d, t) in memo:
                    return memo[(d, t)]
                else:
                    temp = sum([rec(d-1, f, t-x) for x in range(1, f+1)])
                    memo[(d, t)] = temp
                    return temp
            memo = {}
            return rec(d, f, target) % mod
        return 0
