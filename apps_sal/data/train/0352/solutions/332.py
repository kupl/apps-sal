class Solution:

    def predecessor(self, word_1, word_2):
        if abs(len(word_1) - len(word_2)) != 1:
            return False
        idx_1 = 0
        idx_2 = 0
        while idx_1 < len(word_1) and idx_2 < len(word_2):
            if word_1[idx_1] != word_2[idx_2]:
                if idx_1 != idx_2:
                    return False
                if len(word_1) < len(word_2):
                    idx_2 += 1
                else:
                    idx_1 += 1
            else:
                idx_1 += 1
                idx_2 += 1
        return True

    def longestStrChain(self, words: List[str]) -> int:
        dict = {}
        dp = [1 for i in range(0, len(words))]
        words.sort(key=len)
        for i in range(0, len(words)):
            words[i] = ''.join(sorted(words[i]))
            if len(words[i]) in list(dict.keys()):
                dict[len(words[i])].append(i)
            else:
                dict[len(words[i])] = [i]
        for i in range(0, len(words)):
            if len(words[i]) + 1 in list(dict.keys()):
                for elem in dict[len(words[i]) + 1]:
                    if self.predecessor(words[elem], words[i]):
                        dp[elem] = max(dp[elem], dp[i] + 1)
        ans = 0
        for i in range(0, len(dp)):
            ans = max(ans, dp[i])
        return ans
