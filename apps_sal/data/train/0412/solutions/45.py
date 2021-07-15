class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        
        memo = defaultdict(int)

        def solve(d, f, target):
            if (d,f,target) in memo:
                return memo[(d,f,target)]
            if d==0:
                if target!=0:
                    return 0
                else:
                    return 1
            dp = 0
            for i in range(1,f+1):
                dp += solve(d-1,f,target-i)
            memo[(d,f,target)] = dp
            return dp
        
        return solve(d,f,target)%(10**9+7)
