import collections


class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        finalDict = collections.defaultdict(int)
        for i in range(len(s)):
            for j in range(i + minSize - 1, min(i + maxSize, len(s))):
                substring = s[i:j + 1]
                if len(set(substring)) <= maxLetters:
                    finalDict[substring] += 1
        return max(finalDict.values()) if finalDict else 0
