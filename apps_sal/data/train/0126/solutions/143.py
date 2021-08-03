class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        newDict = {}

        for j in range(len(s) - minSize + 1):
            word = s[j:j + minSize]

            if word in newDict:
                newDict[word] += 1

            else:
                if len(collections.Counter(word)) <= maxLetters:
                    newDict[word] = 1

        return max(newDict.values()) if len(newDict) != 0 else 0
