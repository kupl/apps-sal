class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        dict = {}
        (left, right) = (0, minSize)
        while left < len(s):
            while right - left <= maxSize and right <= len(s):
                sub = s[left:right]
                if self.isSize(sub, minSize, maxSize) and self.isUniqueAmount(sub, maxLetters):
                    self.addToDict(sub, dict)
                right += 1
            left += 1
            right = left + minSize
        retValue = 0
        for (k, v) in list(dict.items()):
            retValue = max(retValue, v)
        return retValue

    def addToDict(self, sub: str, dict: {}) -> None:
        if sub not in dict:
            dict[sub] = 0
        dict[sub] += 1

    def isSize(self, s: str, minSize: int, maxSize: int) -> bool:
        length = len(s)
        return minSize <= length and maxSize >= length

    def isUniqueAmount(self, s: str, maxLetters: int) -> bool:
        return len(set(s)) <= maxLetters
