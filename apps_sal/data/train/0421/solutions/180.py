import numpy as np


class Solution:
    def lastSubstring(self, s: str) -> str:
        mx = max(s)

        values = np.array(list(s))
        mxelement = np.where(values == mx)[0]

        mxstring = ''
        for i in mxelement:
            if s[i:] > mxstring:
                mxstring = s[i:]
        return mxstring
