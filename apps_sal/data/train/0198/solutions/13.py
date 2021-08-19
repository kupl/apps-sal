import numpy as np


class Solution:

    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        i = result = 0
        for j in range(len(s)):
            maxCost -= abs(ord(s[j]) - ord(t[j]))
            while maxCost < 0:
                maxCost += abs(ord(s[i]) - ord(t[i]))
                i += 1
            result = max(result, j - i + 1)
        return result
