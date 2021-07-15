class Solution:
    def countVowelPermutation(self, n: int) -> int:  
        # a -> e
        # e -> a,i
        # i -> a,e,o,u
        # o -> i,u
        # u -> a
        rules = [[1,2,4],[0,2],[1,3],[2],[2,3]]
        dp = [1]*5
        
        for i in range(1,n):
            dp_new = [0]*5
            for j in range(5):
                for k in rules[j]:
                    dp_new[j] += dp[k]%(10**9+7)
            dp = dp_new
            
        return sum(dp)%(10**9+7)
        


