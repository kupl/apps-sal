class Solution:
    # sort from smallest to largest length
    # for each element, see if any words of its length - 1 are predescessors
    # for every predecessor, take the max of the word chains and store it + 1
    def isPredecessor(self, prev_word, cur_word):
        if len(prev_word) != len(cur_word) - 1:
            return False
        skipped_char = False
        for i in range(len(prev_word)):
            if not skipped_char and prev_word[i] != cur_word[i]:
                skipped_char = True
            if skipped_char and prev_word[i] != cur_word[i + 1]:
                return False
        return True

    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda word: len(word))
        num_words = len(words)
        chain_lengths = [1 for _ in range(num_words)]
        max_chain_length = 0
        for i in range(num_words):
            for j in range(0, i):
                if len(words[j]) == len(words[i]) - 1 and chain_lengths[j] + 1 > chain_lengths[i] and self.isPredecessor(words[j], words[i]):
                    chain_lengths[i] = chain_lengths[j] + 1
            max_chain_length = max(max_chain_length, chain_lengths[i])
        return max_chain_length
