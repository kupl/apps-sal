class Solution:
    def predecessor(self, word, candidate):
        if len(word) != len(candidate) + 1:
            return False
        j = 0
        for i, c in enumerate(word):
            if i > j + 1 or j == len(candidate):
                break
            if c == candidate[j]:
                j += 1
        return j == len(candidate)

    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        dp = [1 for _ in words]
        for i in range(len(words)):
            for j in range(i, -1, -1):
                if len(words[i]) - len(words[j]) > 1:
                    break
                if self.predecessor(words[i], words[j]):
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
