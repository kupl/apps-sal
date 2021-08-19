from collections import Counter


class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        freq = Counter()
        for k in range(minSize, maxSize + 1):
            for i in range(len(s) - k + 1):
                substring = s[i:i + k]
                if len(set(substring)) <= maxLetters:
                    freq[substring] += 1
        return max(freq.values()) if len(freq) > 0 else 0
