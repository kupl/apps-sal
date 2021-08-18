class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        words.sort(key=len)
        f = [1] * n

        def ispre(w1, w2):
            if len(w1) != len(w2) - 1:
                return False

            it = iter(w2)
            return all(c in it for c in w1)

        res = 1
        for i in range(1, n):
            for j in range(i):
                if ispre(words[j], words[i]):
                    f[i] = max(f[i], f[j] + 1)
            res = max(res, f[i])
        return res
