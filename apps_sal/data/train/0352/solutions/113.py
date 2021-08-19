class Solution:

    def is_chainable(self, shorter, longer):
        for i in range(len(longer)):
            if shorter == longer[:i] + longer[i + 1:]:
                return True
        return False

    def longestStrChain(self, words: List[str]) -> int:
        sw = sorted(words, key=lambda x: len(x))
        n_words = len(sw)
        chains = [1] * n_words
        out = 1
        for i in range(n_words):
            word = sw[i]
            for j in range(i + 1, n_words):
                next_word = sw[j]
                if len(word) == len(next_word):
                    continue
                elif len(word) - len(next_word) != -1:
                    break
                if self.is_chainable(word, next_word):
                    chains[j] = chains[i] + 1
                    out = max(out, chains[j])
        return out
