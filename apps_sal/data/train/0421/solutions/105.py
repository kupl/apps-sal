class Solution:
    def lastSubstring(self, s: str) -> str:
        if not s:
            return None
        mxm = s[:]
        for i in range(len(s)):
            if s[i] >= mxm[0]:
                if s[i:] > mxm:
                    mxm = s[i:]
        return mxm
