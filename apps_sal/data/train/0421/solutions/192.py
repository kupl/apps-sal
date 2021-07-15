class Solution:

    def lastSubstring(self,s: str) -> str:
        result = s
        for i in range(len(s)):
            if s[i:]>result:
                result = s[i:]
        return result

