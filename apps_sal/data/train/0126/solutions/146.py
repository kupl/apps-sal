class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:

        candidates = collections.Counter()

        for i in range(len(s) - minSize + 1):
            if len(set(list(s[i:i + minSize]))) <= maxLetters:
                candidates[s[i:i + minSize]] += 1

        return max(list(candidates.values()) + [0])
