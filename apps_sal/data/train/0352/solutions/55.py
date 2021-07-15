class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = lambda x: len(x))                      # words from short to long 
        counter = {}                                            
        minLen = len(words[0])                                  # minimum length of word
        maxLen = 1
        for idx in range(len(words)):
            if len(words[idx]) == minLen:
                counter[idx] = 1                                # base case 
            else:
                ancestor = 1
                j = 0 
                while idx - j >= 0 and len(words[idx-j]) >= len(words[idx]) - 1:
                    j += 1
                    if len(words[idx-j]) == len(words[idx]):    # do not check words with the same length 
                        continue 
                    if self.checker(words[idx-j], words[idx]):       # check if words[idx-j] is an ancestor of words[idx]
                        #print(words[idx-j], words[idx])
                        ancestor = max(ancestor, counter[idx-j] + 1)
                counter[idx] = ancestor 
                maxLen = max(maxLen, ancestor)
        return maxLen
     
    
    def checker(self, short, long):
        for idx in range(len(long)):
            removed = long[0:idx] + long[idx+1:]
            if short == removed:
                return True 
        return False 
