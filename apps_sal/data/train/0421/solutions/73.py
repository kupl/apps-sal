class Solution:
    def lastSubstring(self, s: str) -> str:
        if not len(s): return s
        temp = s[0]
        for i in range(1,len(s)):
            if s[i:min(i+len(temp), len(s))] > temp:
                temp = s[i]
            else:
                temp += s[i]
        return temp
        

