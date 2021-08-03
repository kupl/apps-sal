class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        if minSize > len(s):
            return 0
        maxCount = 0
        seenSubstrs = Counter()
        for i in range(len(s)):
            letterSet = set()
            for j in range(i, i + minSize - 1):
                if j >= len(s):
                    break
                letterSet.add(s[j])
                if len(letterSet) > maxLetters:
                    break
            if len(letterSet) > maxLetters:
                continue
            for j in range(i + minSize - 1, i + maxSize + 1):
                if j >= len(s):
                    break
                letterSet.add(s[j])
                if len(letterSet) > maxLetters:
                    break
                seenSubstrs[s[i:j + 1]] += 1
                maxCount = max(seenSubstrs[s[i:j + 1]], maxCount)
        return maxCount
