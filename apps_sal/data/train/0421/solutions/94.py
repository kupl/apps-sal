class Solution:

    def lastSubstring(self, s: str) -> str:
        mc = ''
        mi = []
        for i in range(len(s)):
            if s[i] >= mc:
                mi.append(i)
                mc = s[i]
        ms = ''
        for i in mi:
            if s[i:] > ms:
                ms = s[i:]
        return ms
