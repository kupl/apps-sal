class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        mem = {}
        def dfs(l, target):
            if((l, target) in mem):
                return mem[(l, target)]
            if(l==d):
                return int(target==0)
            MOD = 1e9+7
            ans=0
            for i in range(1, f+1):
                ans = (ans+dfs(l+1, target-i))%MOD
            mem[(l, target)] = ans
            return ans
        return int(dfs(0, target))
