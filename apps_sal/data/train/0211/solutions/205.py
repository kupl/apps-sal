class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        self.ans = 0
        seen = set()
        
        def dp(i):
            if i == len(s):
                self.ans = max(self.ans, len(seen))
            
            for j in range(i, len(s)):
                word = s[i:j+1]
                if word not in seen:
                    seen.add(word)
                    dp(j+1)
                    seen.discard(word)
                    
        dp(0)
        return self.ans
