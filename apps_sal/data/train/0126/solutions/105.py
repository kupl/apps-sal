class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        counter = dict()
        n = len(s)
        for i in range(n - minSize + 1):
            for j in range(i + minSize - 1, i + maxSize):
                if j >= n:
                    break
                if len(set(s[i:j + 1])) <= maxLetters:
                    counter[s[i:j + 1]] = counter.get(s[i:j + 1], 0) + 1

        if list(counter.values()) == []:
            return 0
        return max(counter.values())
