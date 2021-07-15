class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = len)
        n = len(words)
        dp = [1] * n
        for i in range(1, n):
            word = words[i]
            word_len = len(word)
            for j in range(0, i):
                if len(words[j]) == word_len - 1:
                    flag = False
                    for t in range(word_len):
                        if word[:t] + word[t+1:] == words[j]:
                            flag = True
                    if flag:
                        dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
                
            
            
        

