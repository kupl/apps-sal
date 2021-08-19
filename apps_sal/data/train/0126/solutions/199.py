class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        res = 0
        count = Counter()
        for j in range(len(s) - minSize + 1):
            if len(set(s[j:j + minSize])) > maxLetters:
                continue
            count[s[j:j + minSize]] += 1
            res = max(res, count[s[j:j + minSize]])
        return res
