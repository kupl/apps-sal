class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        count = collections.Counter(s[i:i+minSize] for i in range(len(s)-minSize+1))
        return max([count[w] for w in count if len(set(w)) <= maxLetters] +[0])
