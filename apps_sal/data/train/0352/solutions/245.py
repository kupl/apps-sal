class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        word_dict = {}
        words = [(len(w), w) for w in words]
        words = sorted(words)

        for _, w in words:
            word_dict[w] = 1

        state_t = set()

        max_chain = 1
        for _, word in words:

            chain_len = word_dict[word]
            max_chain = max(max_chain, chain_len)
            for i in range(len(word) + 1):
                for c in range(97, 123):

                    new_word = word[:i] + chr(c) + word[i:]

                    if word_dict.get(new_word, False) and new_word not in state_t:

                        state_t.add(new_word)
                        word_dict[new_word] = chain_len + 1

        return max_chain
