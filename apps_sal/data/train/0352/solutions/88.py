class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def is_predecessor(w1, w2):
            for i, w in enumerate(w1):
                if(w != w2[i]):
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
                elif(len_i == len_j):
                    continue
                if(combos[i] < combos[j] + 1
                   and is_predecessor(words[i], words[j])):
                    combos[i] = combos[j] + 1

        return max(combos) + 1
