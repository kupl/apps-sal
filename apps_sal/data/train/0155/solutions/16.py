class Solution:
    def maxJumps(self, lst: List[int], d: int) -> int:
        
        
        
        def Ab(i,d,X):
            if i<0 or i>= len(lst):
                return -1
            
            if X<=lst[i]:
                return None
            
            if dp[i] != -1:
                return dp[i]
            m = 1
            for j in range(1,d+1):
                a = 0
                a = Ab(i-j,d,lst[i])
                if a == None:
                    break                
                m = max(m,1+a)
                              
            for j in range(1,d+1):
                b = 0
                b = Ab(i+j,d,lst[i])
                if b == None:
                    break                
                m = max(m,1+b)
            dp[i] = m
            return dp[i]
        dp = [-1 for i in lst]
        for i in range(len(lst)-1,-1,-1):
            Ab(i,d,sys.maxsize)
        return max(dp)
