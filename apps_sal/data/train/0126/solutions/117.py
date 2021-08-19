class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        store = collections.defaultdict(int)
        for i in range(0, len(s) - minSize + 1):
            for j in range(0, maxSize - minSize + 1):
                if i + j + minSize > len(s):
                    break
                subS = s[i:i + minSize + j]
                checkSize = set(subS)
                if len(checkSize) <= maxLetters:
                    store[subS] += 1
        maxNum = 0
        for (key, val) in store.items():
            if val > maxNum:
                maxNum = val
        return maxNum
