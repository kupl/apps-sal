class Solution(object):
    def profitableSchemes(self, G, P, group, profit):       
        mod = 10**9+7
        dp = [[0 for _ in range(G+1)] for _ in range(P+1)] 
        dp[0][0]=1
        for g,p in zip(group,profit):
            cur = [row[:] for row in dp]
            for g_pre in range(G-g+1):
                for p_pre in range(P+1):
                    p_now = min(P,p_pre+p)
                    cur[p_now][g_pre+g]+=dp[p_pre][g_pre]
            dp = cur
            
        return sum(dp[-1])%mod
            

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

