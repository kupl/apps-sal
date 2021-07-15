class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        
        onetime = False
        if minSize == maxSize:
            onetime = True
            
        valid_candidates = {}
        maxoccurrences = 0
        
        def check_candidates(test):
            nonlocal maxoccurrences
            
            if len(set(test)) <= maxLetters:
                valid_candidates[test] = valid_candidates.get(test, 0) + 1
                maxoccurrences = max(maxoccurrences, valid_candidates[test])
                
        #find all possible substrings
        for i in range(len(s)):
            for j in range(minSize, maxSize+1):
                if i + j <= len(s):
                    check_candidates(s[i:i+j])
        
        return maxoccurrences
