class Solution:
    def checkPredecessor(self, word_1, word_2):
        find_extra = False
        for i in range(len(word_1)):
            chr_1 = word_1[i]
            if not find_extra:
                chr_2 = word_2[i]
            else:
                chr_2 = word_2[i + 1]
            if chr_1 != chr_2:
                if find_extra:
                    return False
                else:
                    if chr_1 != word_2[i + 1]:
                        return False
                    find_extra = True
        return True

    def longestStrChain_old(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))
        longest_seq = [1] * len(words)
        for i in range(1, len(words)):
            curr_word = words[i]
            for j in range(0, i)[::-1]:
                prev_word = words[j]
                if len(prev_word) == len(curr_word):
                    continue
                if len(prev_word) + 1 < len(curr_word):
                    break
                if self.checkPredecessor(prev_word, curr_word):
                    longest_seq[i] = max(longest_seq[i], longest_seq[j] + 1)
        return max(longest_seq)

    def longestStrChain(self, words):
        words.sort(key=lambda x: len(x))
        longest_chain = {}

        for word in words:
            longest_chain[word] = max([longest_chain.get((word[:i] + word[i + 1:]), 0) for i in range(len(word))]) + 1

        return max(longest_chain.values())
