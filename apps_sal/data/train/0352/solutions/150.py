class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key=lambda w: len(w))

        seenCache = {}
        max_len = 0

        for cur_word in words:
            # print(cur_word)
            cur_len = 0
            for i in range(len(cur_word)):
                check_word = cur_word[:i] + cur_word[i + 1:]
                cur_len = max(cur_len, seenCache.get(check_word, 0) + 1)

            seenCache[cur_word] = cur_len
            max_len = max(max_len, cur_len)

        return max_len
