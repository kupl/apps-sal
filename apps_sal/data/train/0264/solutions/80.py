class Solution:
    def maxLength(self, arr) -> int:
        maxLen = 0
        arr = sorted(arr, key=lambda x: len(x), reverse=True)
        self.compatible = {}
        for i in range(len(arr)):
            currString = arr[i]
            if self.noDupes(currString):
                if currString not in self.compatible:
                    self.compatible[currString] = []
                for j in range(i + 1, len(arr)):
                    if self.noDupes(arr[j]) and self.uniqueChars(currString, arr[j]):
                        self.compatible[currString].append(arr[j])
        for key in self.compatible:
            if len(self.compatible[key]) == 0:
                length = len(key)
            else:
                length = self.findLength(key, key, 0)
            maxLen = max(maxLen, length)
        return maxLen

    def uniqueChars(self, s1, s2):
        for c in s2:
            if c in s1:
                return False
        return True

    def noDupes(self, string):
        counts = {}
        for c in string:
            counts[c] = counts.get(c, 0) + 1
            if counts[c] > 1:
                return False
        return True

    def findLength(self, currString, totalString, maxLen):
        for string in self.compatible[currString]:
            if self.uniqueChars(totalString, string):
                maxLen = max(maxLen, self.findLength(string, totalString + string, len(totalString) + len(string)))

        return maxLen
