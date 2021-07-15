# from function
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        res=0
        mod=10**9+7
        @lru_cache(maxsize=None)
        def dfs(n,val,count):
            if not n:
                return 1
            t=0
            for i in range(6):
                if i!=val:
                    t+=dfs(n-1,i,1)
                elif i==val and  count<rollMax[i]:
                    t+=dfs(n-1,val,count+1)
            # t%=mod
            return t
        return sum(dfs(n-1,i,1) for i in range(6))%mod
