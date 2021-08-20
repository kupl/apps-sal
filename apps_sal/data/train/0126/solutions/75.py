class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        (occ, n) = ({}, len(s))
        for i in range(n):
            for j in range(i + minSize - 1, min(i + maxSize, n)):
                sub = s[i:j + 1]
                if len(set(sub)) <= maxLetters:
                    occ[sub] = occ.get(sub, 0) + 1
        return max(list(occ.values()) or [0])
