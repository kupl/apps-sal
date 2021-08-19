class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        if not words:
            return 0
        words.sort(key=lambda x: len(x))
        dp = [1] * len(words)
        for i in range(len(words)):
            curr = words[i]
            for j in range(i):
                prev = words[j]
                if self.checkPredecessor(curr, prev):
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def checkPredecessor(self, curr, prev):
        if len(curr) - len(prev) != 1:
            return False
        i = j = 0
        diff = False
        while i < len(curr) and j < len(prev):
            if curr[i] == prev[j]:
                i += 1
                j += 1
            else:
                if diff:
                    return False
                diff = True
                i += 1
        return True
