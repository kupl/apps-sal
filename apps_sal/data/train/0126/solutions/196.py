class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        count = defaultdict(int)
        m = 0
        size = minSize
        for i in range(len(s) - size + 1):
            word = s[i:i + size]
            if len(Counter(word)) <= maxLetters:
                count[word] += 1
                m = max(m, count[word])
        return m
