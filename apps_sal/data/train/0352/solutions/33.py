class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        lengthMap = {}
        for word in words:
            n = len(word)
            if n not in lengthMap:
                lengthMap[n] = []
            lengthMap[n].append(word)
        arr = [0 for i in range(len(words))]
        dp = {i: -1 for i in words}
        res = 1
        for i in range(len(words)):
            arr[i] = self.get_longest(dp, lengthMap, words[i])
            res = max(arr[i], res)
        print(arr)
        return res

    def get_longest(self, dp, lengthMap, word):
        if dp[word] != -1:
            return dp[word]
        if len(word) + 1 not in lengthMap:
            return 1
        res = 0
        for item in lengthMap[len(word) + 1]:
            if self.only_one_diff(word, item):
                res = max(res, self.get_longest(dp, lengthMap, item))
        dp[word] = res + 1
        return res + 1

    def only_one_diff(self, word1, word2):
        for i in range(len(word2)):
            if word2[:i] + word2[i + 1:] == word1:
                return True
        return False
