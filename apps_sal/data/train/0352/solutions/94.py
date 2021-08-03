class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def is_predecessor(w1, w2):
            for i in range(len(w1)):
                if(w1[i] != w2[i]):
                    return w1[i:] == w2[i + 1:]

            return True

        words.sort(key=len, reverse=True)
        len_words = len(words)
        combos = [0] * len_words

        for i in range(len_words):
            for j in reversed(list(range(0, i))):
                len_i, len_j = len(words[i]), len(words[j])
                if(len_i + 1 < len_j):
                    break
                if(len_i + 1 == len_j
                   and combos[i] < combos[j] + 1
                   and is_predecessor(words[i], words[j])):
                    combos[i] = combos[j] + 1

        # for i in range(len_words):
        #     print(combos[i], end=', ')
        #     print(words[i])

        return max(combos) + 1
