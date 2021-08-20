class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        words.sort(key=len)
        f = [1] * n

        def ispre(w1, w2):
            if len(w1) != len(w2) - 1:
                return False
            i = j = 0
            diff = False
            while i < len(w1) and j < len(w2):
                if w1[i] != w2[j]:
                    if not diff:
                        diff = True
                        j += 1
                        continue
                    else:
                        return False
                i += 1
                j += 1
            return True
        res = 1
        for i in range(1, n):
            for j in range(i):
                if ispre(words[j], words[i]):
                    f[i] = max(f[i], f[j] + 1)
            res = max(res, f[i])
        return res
