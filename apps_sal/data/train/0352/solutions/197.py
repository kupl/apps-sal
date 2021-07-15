class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words=sorted(words,key=lambda x:len(x))
        def helper(w1,w2):
            if len(w2)-len(w1)!=1:return False
            i,j=0,0
            while i<len(w1) and j<len(w2):
                if w1[i]==w2[j]:
                    i+=1
                j+=1
            return i==len(w1)
        n=len(words)
        dp=[1 for i in range(n)]
        for i in range(n):
            for j in range(i):
                if helper(words[j],words[i]):
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # words=sorted(words,key=lambda x:len(x))
        # def ccmp(a,b):
        #     if len(b)-len(a)!=1:
        #         return False
        #     i,j=0,0
        #     while i<len(a) and j <len(b):
        #         if a[i]==b[j]:
        #             i+=1
        #             j+=1
        #         else:
        #             j+=1
        #     return i==len(a)
        # n=len(words)
        # dp=[1 for i in range(n)]
        # for i in range(1,n):
        #     for j in range(i):
        #         if len(words[i])-len(words[j])==1:
        #             if ccmp(words[j],words[i]): 
        #                 dp[i]=max(dp[i],dp[j]+1)
        # ans=0
        # for i in range(n):
        #     ans=max(ans,dp[i])
        # return ans
                    
                
                    

