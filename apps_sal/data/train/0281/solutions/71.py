class Solution:

    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        counts = [0] * 26
        for (si, ti) in zip(s, t):
            difference = ord(ti) - ord(si)
            if difference < 0:
                difference += 26
            counts[difference] += 1
        for (i, count) in enumerate(counts[1:], 1):
            maxConvert = i + 26 * (counts[i] - 1)
            if maxConvert > k:
                return False
        return True
