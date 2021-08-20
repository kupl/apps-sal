import numpy as np


class Solution:

    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        Ss = [ord(c) for c in s]
        Tt = [ord(d) for d in t]
        diff = np.abs(np.array(Ss) - np.array(Tt))
        n = len(diff)
        i = result = 0
        for j in range(n):
            maxCost -= diff[j]
            if maxCost < 0:
                maxCost += diff[i]
                i += 1
            result = max(result, j - i + 1)
        return result
