import numpy as np


class Solution:
    def lastSubstring(self, s: str) -> str:
        mx = max(s)
        #mxelement = [i for i, j in enumerate(s) if j == mx]

        values = np.array(list(s))
        mxelement = np.where(values == mx)[0]

        mxstring = ''
        for i in mxelement:
            if s[i:] > mxstring:
                mxstring = s[i:]
        return mxstring
