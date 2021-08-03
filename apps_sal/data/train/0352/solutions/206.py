class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda w: len(w))

        word_chains = {w: 1 for w in words}

        # intentionally min length to max length
        for word in words:
            for i in range(len(word)):
                sub_word = word[:i] + word[i + 1:]
                if sub_word in words:
                    word_chains[word] = max(word_chains[sub_word] + 1, word_chains[word])

        return max(word_chains.values())
