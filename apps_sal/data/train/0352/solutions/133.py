class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def isPred(w1,w2):
            if len(w1)!=(len(w2)-1):
                return False
            i,j = 0,0
            while i<len(w1):
                if w1[i]!=w2[j]:
                    if i!=j:
                        return False
                    j+=1
                else:
                    i+=1
                    j+=1
            return True
           
        words=sorted(words,key=lambda x: len(x))
        dp = [1]*len(words)
        for i in range(len(words)):
            for j in range(i): 
                if isPred(words[j],words[i]):
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)
            

