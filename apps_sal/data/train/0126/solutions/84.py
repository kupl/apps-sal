import collections
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        substrings = []
        for size in range(minSize, maxSize + 1):
            for i in range(len(s)-size+1):
                if len(set(s[i:i+size])) <= maxLetters:
                    substrings.append(s[i:i+size])
        return collections.Counter(substrings).most_common(1)[0][1] if substrings else 0

