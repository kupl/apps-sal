class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = len)
        dp = [1]*len(words)
        m = 1
        for i in range(1, len(words)):
            j = i-1
            cl = len(words[i])
            while(len(words[j]) >= cl-1 and j>-1):
                if(len(words[j]) == cl):
                    j-=1
                    continue
                f = 0
                w1, w2 = words[i], words[j]
                li, lj = 0,0
                while(f<2 and lj < len(w2)):
                    if(w1[li] == w2[lj]):
                        li+=1
                        lj+=1
                    else:
                        f+=1
                        li+=1
                if(f!=2):
                    dp[i] = max(dp[i], 1 + dp[j])
                    m = max(dp[i], m) 
                j-=1
        return m  
                   

