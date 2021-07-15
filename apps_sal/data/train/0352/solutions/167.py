class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        
        def helper(a,b):
            i,j = 0,0
            diff = 0
            while(i<len(a) and j<len(b)):
                
                if a[i] == b[j]:
                    i+=1
                    j+=1
                else:
                    i+=1
                    diff+=1
            if i<len(a):
                diff+=(len(a)-i)
            if j<len(b):
                diff+=(len(b)-j)
                            
            if diff>1:
                return False
            else:
                return True
                    
        dp = [1]*(len(words))
        words = sorted(words,key=len)
        
        for i in range(len(words)):
            for j in range(i):
                if len(words[i])-len(words[j]) == 1 and helper(words[i],words[j]):
                    dp[i] = max(dp[i],dp[j]+1)
        print(dp)     
        return max(dp)
                    
        
        
        

