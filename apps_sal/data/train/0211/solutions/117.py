class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
        ans = 0
        for i in range(1, 2**(len(s) - 1) + 1):    
            prev = 0
            seen = set()
            for j in range(0, len(s)):
                if i & (1 << j):
                    seen.add(s[prev:(j+1)])
                    prev = j + 1
            final = s[prev:len(s)]
            if len(final):
                seen.add(final)
            ans = max(ans, len(seen))
        return ans
