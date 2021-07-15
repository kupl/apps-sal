class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        def isPre(st1,st2):
            if len(st2)!=len(st1)+1:
                return False
            j=0
            diff=0
            for i in range(len(st2)):
                if diff>1:
                    return False
                elif j<len(st1) and st1[j]==st2[i]:
                    j+=1
                else:
                    diff+=1
            return diff<=1

        words.sort(key=lambda x: len(x))
        n=len(words)
        dp=[1]*n
        #print(words)
        for i in range(1,n):
            for j in range(i):
                if isPre(words[j],words[i]):
                    dp[i]=max(dp[i],dp[j]+1)
        #print([(words[i],dp[i]) for i in range(n)])
        return max(dp)
