class Solution:
    mod=(10)**9+7
    relation=[[1,2,4],[0,2],[1,3],[2],[2,3]]
    def dfs(self,n,v):
        memo=self.memo
        if n==1:
            return 1
        if memo[n][v]!=-1:
            return memo[n][v]
        memo[n][v]=0
        ans=0
        for i in self.relation[v]:
            ans=(ans+self.dfs(n-1,i))%self.mod
        memo[n][v]=ans
        return ans
        
            
    def countVowelPermutation(self, n: int) -> int:
        self.memo=[[-1 for _ in range(5)] for _ in range(n+1)]
        res=0
        for i in range(5):
            res=(res+self.dfs(n,i))%self.mod
        return res            
         
        
        
        
        
        

