class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        if not words:return 0
        
        words.sort(key=lambda x:len(x))
        
        counter=[collections.Counter(word) for word in words]
        
        dp=[1]*len(words)
        maxlen=0
        for i in range(len(dp)):
            for j in range(i):
                if len(words[i])-len(words[j])==1 and len((counter[i]-counter[j]))==1:
                    dp[i]=max(dp[i],1+dp[j])
                    
            maxlen=max(maxlen,dp[i])
            
            
        return maxlen
                

