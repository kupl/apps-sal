from collections import defaultdict


class Solution:
    def is_one_apart(self, word1, word2):
        assert len(word1) >= len(word2)

        length_diff = len(word1) - len(word2)
        if length_diff != 1:
            return False

        i = 0
        j = 0
        while i < len(word1) and j < len(word2):
            if word1[i] == word2[j]:
                i += 1
                j += 1
            elif i - j >= 1:
                return False
            else:
                i += 1

        return True

    def longestStrChain(self, words: List[str]) -> int:
        length_words = defaultdict(list)
        chain_lengths = {}
        max_chain = 1

        for word in words:
            length_words[len(word)].append(word)
            chain_lengths[word] = 1

        for length in sorted(list(length_words.keys()), reverse=True):
            if length - 1 not in length_words:
                continue

            for word1 in length_words[length]:
                for word2 in length_words[length - 1]:
                    if chain_lengths[word1] + 1 <= chain_lengths[word2]:
                        continue

                    if self.is_one_apart(word1, word2):
                        chain_lengths[word2] = chain_lengths[word1] + 1
                        max_chain = max(max_chain, chain_lengths[word2])

        return max_chain
