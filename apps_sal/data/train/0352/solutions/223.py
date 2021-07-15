class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        ## return a list of lists
        #words.sort(cmp=lambda x,y:len(x) - len(y))
        words = sorted(words, key = lambda x: len(x))
        #print(words)
        dp = [1]*len(words)
        res = 1
        for i in range(len(words)):
            for j in range(0,i):
                ## compare word[j] -> word[i]
                #print(self.isPrecessor(words[j],words[i]))
                if len(words[i])>len(words[j]) and self.isPrecessor(words[j],words[i]):
                    dp[i] = max(dp[i],dp[j]+1)
                    res = max(res,dp[i])
        #print(dp)            
        return res
    
    def isPrecessor(self,word1,word2):
        #print('------------')
        #print(word1)
        #print(word2)
        ind1 = 0
        ind2 = 0
        flag = 0
        
        while ind1<len(word1) and ind2<len(word2):
            if word1[ind1]==word2[ind2]:
                ind1 += 1
                ind2 += 1
            else: 
                if flag==1:
                    return False
                ind2 += 1
                flag = 1
                
        return (ind1==len(word1) and ind2==len(word2)) or (ind1==len(word1) and flag==0 and (ind2+1)==len(word2))

