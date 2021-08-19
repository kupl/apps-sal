class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        if len(s) == len(set(s)):
            return 0
        from collections import defaultdict
        corpus = defaultdict(int)
        for i in range(minSize, maxSize + 1):
            for j in range(len(s) - i + 1):
                if len(set(s[j:j + i])) <= maxLetters:
                    corpus[s[j:j + i]] += 1
        if len(corpus) == 0:
            return 0
        return max(corpus.values())
