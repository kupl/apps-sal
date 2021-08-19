class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        count = collections.Counter()
        for i in range(len(s) - minSize + 1):
            t = s[i:minSize + i]
            if len(set(t)) <= maxLetters:
                count[t] += 1
        if count:
            return max(count.values())
        else:
            return 0
