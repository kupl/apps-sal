class Solution:
    def longestPrefix(self, s: str) -> str:
        long = 0
        for x in range(0,len(s)-1):
            a = s[0:x+1]
            b = s[len(s)-1-x:]
            if a==b:
                long = max(long, len(a))
        return s[:long]
