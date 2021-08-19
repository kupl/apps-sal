class Solution:

    def issubsequence(self, str1, str2):
        str1_pointer = 0
        for i in range(len(str2)):
            if str2[i] == str1[str1_pointer]:
                str1_pointer += 1
            if str1_pointer == len(str1):
                return True
        return False

    def longestStrChain(self, words: List[str]) -> int:
        word_lengths = {}
        for i in words:
            if len(i) not in word_lengths:
                word_lengths[len(i)] = [i]
            else:
                word_lengths[len(i)].append(i)
        max_length = max(list(word_lengths.keys()))

        @lru_cache(None)
        def dp(word):
            if len(word) not in word_lengths:
                return 0
            if len(word) == max_length:
                return 1
            else:
                max_chain = 1
                for i in word_lengths[len(word) + 1]:
                    if self.issubsequence(word, i):
                        max_chain = max(max_chain, 1 + dp(i))
                return max_chain
        res = 0
        for i in words:
            res = max(res, dp(i))
        return res
