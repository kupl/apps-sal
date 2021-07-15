class Solution:
    def IsPredecessor(self, w1, w2):
        # return true if w2 is predecessor of w1
        if len(w1)+1 != len(w2):
            return False
        if len(w1)==0:
            return True  

        diff = 0
        for i in range(len(w2)):
            if i-diff==len(w1) or w1[i-diff] != w2[i]:
                diff += 1

        return diff==1
        
    def longestStrChain(self, words: List[str]) -> int:
         
        if len(words)<1:
            return 0
        
        # Use a hashmap to record the length and the index
        length_position = [[] for i in range(17)]
        for i in range(len(words)):
            w = words[i]
            length_position[len(w)].append(i)
                  
        dp = [1]*len(words)
        
        # visit the dictionaty from shorter length to longer length
        for i in range(2, 17):
            if len(length_position[i-1])==0 or len(length_position[i])==0:
                continue
            current = length_position[i]
            previous = length_position[i-1]
            for j in current:
                for k in previous:
                    if self.IsPredecessor(words[k], words[j]):
                        dp[j] = max(dp[j], dp[k]+1)
        return max(dp)
