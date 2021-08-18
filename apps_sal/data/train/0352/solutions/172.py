class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        words = sorted(words, key=lambda x: len(x))
        DP = [0 for i in words]

        max_len = 0
        for i in range(len(words)):
            length = []
            for j in range(1, i + 1):
                if len(words[i - j]) < len(words[i]) - 1:
                    break
                else:
                    if len(words[i - j]) == len(words[i]) - 1:
                        if self.check(words[i - j], words[i]) == True:
                            length.append(DP[i - j])
            if length:
                DP[i] = max(length) + 1
            else:
                DP[i] = 1
        return max(DP)

    def check(self, word1, word2):
        val = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                if val == 0:
                    word2 = word2[:i] + word2[i + 1:]
                    return word1 == word2

                if val == 1:
                    return False
                continue
        return True
