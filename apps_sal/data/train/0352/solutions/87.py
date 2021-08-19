from collections import Counter, defaultdict


class Solution:

    def is_one_away(self, c_1, c_2) -> bool:
        diff = 0
        for (k, v) in list(c_2.items()):
            diff += v - c_1.get(k, 0)
            if diff > 1:
                return False
        for k in c_1:
            if k not in c_2:
                return False
        return True

    def helper(self, word, words_for_len, counters_for_words):
        w_counter = counters_for_words[word]
        max_chain = 0
        for w in words_for_len[len(word) + 1]:
            if self.is_one_away(w_counter, counters_for_words[w]):
                max_chain = max(max_chain, self.helper(w, words_for_len, counters_for_words))
        return max_chain + 1

    def longestStrChain(self, words: List[str]) -> int:
        words_for_len = defaultdict(list)
        counters_for_words = {w: Counter(w) for w in words}
        for w in words:
            words_for_len[len(w)].append(w)
        max_chain = 0
        for w in words:
            max_chain = max(max_chain, self.helper(w, words_for_len, counters_for_words))
        return max_chain
