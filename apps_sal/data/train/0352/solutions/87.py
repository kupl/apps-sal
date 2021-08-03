from collections import Counter, defaultdict


class Solution:
    def is_one_away(self, c_1, c_2) -> bool:
        # c_1 will be shorter than c_2
        diff = 0
        for k, v in list(c_2.items()):
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
        # Logic:
        # define the longest string chain starting at word w as L[w]
        #   L[w] = 1 + max over all w' in W such that dist(w, w') == 1(L[w'])
        # Compute map of length to word counters to easily find all words 1 letter increased from a given word
        # Given some w,
        #     max_chain := 0
        #     For all w' one letter away
        #          max_chain := max(max_chain, max_chain(w')) + 1
        # return max_chain
        # Time Complexity analysis: ??
        # Space: recursive stack O(n) will be the depth of the tree, hashmap O(n)
        words_for_len = defaultdict(list)
        counters_for_words = {w: Counter(w) for w in words}
        for w in words:
            words_for_len[len(w)].append(w)

        max_chain = 0
        for w in words:
            max_chain = max(max_chain, self.helper(w, words_for_len, counters_for_words))
        return max_chain
