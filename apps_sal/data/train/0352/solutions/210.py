class Solution:

    def longestStrChain(self, words: List[str]) -> int:

        def pre(word2, word):
            if len(word2) + 1 == len(word):
                for i in range(len(word)):
                    if word[:i] + word[i + 1:] == word2:
                        return True
            return False
        words = sorted(words, key=lambda x: -len(x))
        best = 0
        n = len(words)
        length = [0] * n
        for i in range(n):
            for j in range(i + 1, n):
                if pre(words[j], words[i]):
                    length[j] = max(length[j], length[i] + 1)
                    best = max(best, length[j])
        return best + 1
