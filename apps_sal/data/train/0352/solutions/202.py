class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        print(words)
        sequence = collections.defaultdict(list)
        dp = [1] * len(words)
        for i in range(len(words)):
            for j in range(0, i):
                predecessor = self.checkPredecessor(words[j], words[i])
                if predecessor:
                    sequence[words[i]].append(words[j])
                    dp[i] = max(dp[j] + 1, dp[i])
        print(sequence)
        print(list(zip(words, dp)))
        return max(dp)

    def checkPredecessor(self, word1, word2):
        if len(word2) - len(word1) > 1:
            return False
        elif len(word1) == len(word2):
            return False
        i = j = 0
        diff = False
        while i < len(word1):
            if word1[i] == word2[j]:
                i += 1
                j += 1
            elif not diff:
                diff = True
                j += 1
            else:
                return False
        if i == len(word1) and j < len(word2) and diff:
            return False
        return True
