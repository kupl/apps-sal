class Solution:
    def lastSubstring(self, s: str) -> str:
        mx = max(s)
        mxelement = [i for i, j in enumerate(s) if j == mx]
        mxstring = ''
        for i in mxelement:
            mxstring = max(s[i:], mxstring)
        return mxstring
