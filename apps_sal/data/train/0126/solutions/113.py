class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        substrings = collections.defaultdict(int)
        for k in range(minSize, maxSize + 1):
            for i in range(len(s) - k + 1):
                substrings[s[i:i + k]] += 1
        maxCount = 0
        for (k, v) in list(substrings.items()):
            if len(set(k)) <= maxLetters:
                maxCount = max(maxCount, v)
        return maxCount
