def find(s1,s2):
    i = 0
    j = 0
    count = 0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            i += 1
            j += 1
        else:
            j += 1
            count += 1
    
    if i == len(s1):
        return True
    if count == 1:
        return True
    
    return False

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        new_words = []
        for w in words:
            new_words.append((len(w),w))
        
        new_words.sort()
        dp = [1]*len(words)
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                l1,w1 = new_words[i]
                l2,w2 = new_words[j]
                if l2-l1 > 1:
                    break
                if l2-l1 == 1:
                    diff = find(w1,w2)
                    if diff == 1:
                        dp[j] = max(dp[j],dp[i]+1)
        
        return max(dp)
