class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        wordCounter = collections.defaultdict()

        # loop (maxSize - minSize)+1 times
        for i in range((maxSize - minSize) + 1):
            charCounter = collections.Counter(s[:minSize + i])
            if len(charCounter) <= maxLetters:
                wordCounter[s[:minSize + i]] = 1

            for j in range(minSize + i, len(s)):
                charCounter[s[j - minSize - i]] -= 1

                if charCounter[s[j - minSize - i]] <= 0:
                    del charCounter[s[j - minSize - i]]

                charCounter[s[j]] += 1
                if len(charCounter) <= maxLetters:
                    if s[j - minSize - i + 1:j + 1] in wordCounter:
                        wordCounter[s[j - minSize - i + 1:j + 1]] += 1
                    else:
                        wordCounter[s[j - minSize - i + 1:j + 1]] = 1

        maxTimes = 0
        for subString in wordCounter:
            maxTimes = max(wordCounter[subString], maxTimes)
        return maxTimes
