from collections import Counter


class Solution:
    def lastSubstring(self, s: str) -> str:
        d = Counter(s)
        if(len(d) == 1):
            return s
        c = sorted(d.keys())[-1]
        i = 0
        while(s[i] != c):
            i += 1
        if(d[c] == 1):
            return s[i:]
        ans = s[i:]
        i += 1
        while(i < len(s)):
            if(s[i] == c and s[i:] > ans):
                ans = s[i:]
            i += 1
        return ans
