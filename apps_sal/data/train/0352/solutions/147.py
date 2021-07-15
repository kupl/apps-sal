from collections import defaultdict
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        def isPartOfChain(longer,shorter):
            if len(longer) - len(shorter) != 1:
                return False 
            
            short_ptr = 0
            long_ptr = 0
            
            num_differences = 0
            while long_ptr <= len(longer):
                
                
                if num_differences > 1:
                    return False

                if short_ptr > len(shorter)-1:
                    break
                
                if shorter[short_ptr] == longer[long_ptr]:
                    short_ptr += 1
                    long_ptr += 1
                
                else:
                    long_ptr += 1
                    num_differences += 1
            
            return True 
            
    
        def longestHelp(words):
            
            
            if len(words) <= 1:
                return 1
            
            
            dp = [1 for _ in range(len(words))]
            
            #dp[i] = longest chain at words[i] 
            
            # max_length is always 1 for each word
            max_length = 1
            for word in range(0,len(dp)):
                for j in range(word-1,-1,-1):
                    if isPartOfChain(words[word], words[j]):
                        dp[word] = max(dp[word],1+dp[j])
                        max_length = max(max_length, dp[word])


            return max_length
        
        words.sort(key = len)
        return longestHelp(words)
        

