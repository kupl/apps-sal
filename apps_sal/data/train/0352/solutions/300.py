class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        word_map = collections.defaultdict(int)
        word_list = collections.defaultdict(list)
        ans = 1
        # 没有任何先导单词的话，is_predecessor 永远返回false, 这样长度至少为1
        for word in words:
            length = len(word)
            word_list[length].append(word)
            word_map[word] = 1

        # print(word_map)
        for word_len in range(1, 17):
            if word_len not in word_list:
                continue
            for word in word_list[word_len]:
                pre_len = word_len - 1
                if pre_len not in word_list:
                    break
                for pre_word in word_list[pre_len]:
                    if self.is_predecessor(pre_word, word):
                        word_map[word] = max(word_map[word], word_map[pre_word] + 1)
                        ans = max(ans, word_map[word])

        return ans

    def is_predecessor(self, w1, w2):
        idx1, idx2 = 0, 0
        once = False
        while idx1 < len(w1) and idx2 < len(w2):
            if w1[idx1] == w2[idx2]:
                idx1 += 1
                idx2 += 1
            elif once:
                return False
            else:
                once = True
                idx2 += 1

        return True
