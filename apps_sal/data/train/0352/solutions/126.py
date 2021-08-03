class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        if len(words) == 0:
            return 0

        def findDistance(shorterString, longerString):
            if len(longerString) - len(shorterString) != 1:
                return False
            i, j = 0, 0
            edits = 0
            while j < len(shorterString):
                if longerString[i] != shorterString[j]:
                    if edits == 0:
                        i += 1
                        edits += 1
                        continue
                    else:
                        return False
                i += 1
                j += 1
            return True

        dp = [1] * len(words)
        words = sorted(words, key=lambda x: len(x))
        maxAnswer = 0
        for i in range(len(words)):
            temp = 1
            for j in range(i + 1):
                if findDistance(words[j], words[i]):
                    temp = max(temp, dp[j] + 1)
            dp[i] = temp
            maxAnswer = max(maxAnswer, dp[i])
        # print(dp)
        return maxAnswer
