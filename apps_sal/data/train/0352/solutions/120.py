class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = [ 1 for i in range(len(words))]
        words.sort(key=lambda x:len(x))
        for i in range(len(words)):
            for j in range(i):
                if len(words[j]) == len(words[i]):
                    continue
                if len(words[i]) - len(words[j]) > 1:
                    continue
                else:
                    count = 0
                    for ch in words[j]:
                        if ch in words[i]:
                            count += 1
                    
                    if count == len(words[j]):
                        dp[i] = dp[j] + 1
        
        return max(dp)
    
                            

