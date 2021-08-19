class Solution:

    def get_dict(self, word):
        d = {}
        for c in word:
            d[c] = d.get(c, 0) + 1
        return d

    def is_close(self, word1, word2):
        dict_word1 = self.get_dict(word1)
        dict_word2 = self.get_dict(word2)
        diff = False
        for (letter, freq) in list(dict_word2.items()):
            if letter in dict_word1:
                if abs(freq - dict_word1[letter]) == 1:
                    if not diff:
                        diff = True
                    else:
                        return False
                elif abs(freq - dict_word1[letter]) > 1:
                    return False
            elif freq > 1:
                return False
            elif not diff:
                diff = True
            else:
                return False
        return True

    def longestStrChain(self, words: List[str]) -> int:
        if not words:
            return 0
        dict_lens = {}
        dict_words = {}
        for word in words:
            dict_lens.setdefault(len(word), []).append(word)
            dict_words[word] = 0
        max_res = 0
        sorted_keys = sorted(dict_lens.keys())
        for len_num in sorted_keys:
            if len_num + 1 in dict_lens:
                next_word_list = dict_lens[len_num + 1]
            else:
                continue
            for word in dict_lens[len_num]:
                for next_word in next_word_list:
                    if self.is_close(word, next_word):
                        dict_words[next_word] = max(dict_words[next_word], dict_words[word] + 1)
                        max_res = max(max_res, dict_words[next_word])
        return max_res + 1
