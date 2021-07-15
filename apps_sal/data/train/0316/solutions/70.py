class Solution:
    def longestPrefix(self, s: str) -> str:
        sLen = len(s)
        if sLen == 1:
            return ''
        
        def happyNow(x):
            if s[:x] == s[-x:]:
                return True
            return False 
        
        for length in range(sLen-1, 0, -1):
            if happyNow(length):
                return s[:length]
        return ''
