import numpy as np


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        #Ss = [ord(c) for c in s]
        #Tt = [ord(d) for d in t]
        #diff = np.abs(np.array(Ss)-np.array(Tt))
        #n = len(s)
        i = result = 0
        for j in range(len(s)):
            maxCost -= abs(ord(s[j]) - ord(t[j]))
            while(maxCost < 0):
                maxCost += abs(ord(s[i]) - ord(t[i]))
                i += 1
            result = max(result, j - i + 1)

        return result
