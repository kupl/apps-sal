class Solution:
    def _check_word(self, wordlong, word2) -> bool:
        if len(wordlong) - len(word2) > 1 or len(wordlong) - len(word2) == 0:
            return False
        for i in range(0, len(wordlong)):
            newstr = wordlong[:i] + wordlong[i + 1:]
            if newstr == word2:
                return True

        return False

    def longestStrChain(self, words: List[str]) -> int:
        if len(words) == 1:
            return words[0]

        words = sorted(words, key=len, reverse=True)

        m = [1] * len(words)
        for i in range(1, len(words)):
            for j in range(0, i):
                if self._check_word(words[j], words[i]) and m[j] + 1 > m[i]:
                    m[i] = m[j] + 1
        return max(m)
