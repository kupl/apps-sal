import numpy as np


class Solution:
    def lastSubstring(self, s: str) -> str:

        input_list = np.array([ord(x) for x in s])
        i, = np.where(input_list == np.max(input_list))

        r = ''
        for e in i:
            r = max(r, s[e:])

        return r
