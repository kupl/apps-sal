class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        
        def dp(s,e):
            if (s,e) in memo:
                return memo[(s,e)]
            ans=2**31
            # print(ans)
            canCut=False
            for cut in cuts:
                # canCut=True
                if s<cut<e:
                    canCut=True
                    a1=dp(s,cut)+dp(cut,e)+e-s
                    # print(a1)
                    ans=min(ans,a1)
            if not canCut:
                # print(\"in\")
                return 0
            memo[(s,e)]=ans
            return ans
        
        memo={}
        return dp(0,n)
        # return count
                    

