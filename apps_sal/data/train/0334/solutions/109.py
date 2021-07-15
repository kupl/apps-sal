class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        n = len(s)
        
        memo = {}
        def f(prev, i):
            if i == n:
                return 0
            
            if (prev, i) in memo:
                return memo[(prev, i)]
            
            if s[i] == prev:
                # No choice, we have to delete s[i]
                memo[(prev, i)] = cost[i] + f(s[i], i + 1)
            elif i + 1 >= n or s[i] != s[i+1]:
                # The next character is the not the same as s[i], no need to delete
                memo[(prev, i)] = f(s[i], i + 1)
            else:
                # The next character exists (i + 1 < n) and it is the same as s[i].
                # We may choose to delete s[i] or not delete s[i], return the min cost
                # of two choices
                memo[(prev, i)] = min(cost[i] + f(prev, i + 1), f(s[i], i + 1))
            
            return memo[(prev, i)]
    
        return f(None, 0)
                      
            
            
            

