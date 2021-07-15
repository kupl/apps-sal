class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        k = minSize
        count = collections.Counter(s[i:i + k] for i in range(len(s) - k + 1))
        return max([count[w] for w in count if len(set(w)) <= maxLetters] + [0])
