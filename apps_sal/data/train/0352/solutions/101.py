class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = len)
        dp = [1 for i in range(len(words))]
        for r in range(1, len(words)):
            for l in range(r):
                if len(words[r]) == len(words[l]) + 1:
                    missingLetters = i = 0
                    for j in range(len(words[r])):
                        if i >= len(words[l]) or words[l][i] != words[r][j]:
                            missingLetters += 1
                            if missingLetters > 1:
                                break
                        else:
                            i += 1
                    if missingLetters == 1:
                        dp[r] = max(dp[r], dp[l] + 1)
        return max(dp)
                
                
                
            
        

