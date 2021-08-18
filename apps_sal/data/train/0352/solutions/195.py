class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        if not words:
            return 0
        self.memo = defaultdict(bool)

        def isPred(p, q, words):
            if (p, q) in self.memo:
                return self.memo[(p, q)]
            w1 = words[p]
            w2 = words[q]
            n2 = len(w2)
            res = False
            for i in range(n2):
                if w1 == w2[0:i] + w2[i + 1:]:
                    res = True
            self.memo[(p, q)] = res
            return res

        n = len(words)

        dpR = [1] * n
        wR = sorted(words, key=len)
        for i in range(n):
            cur = 1
            for j in range(i):
                n1 = len(wR[j])
                n2 = len(wR[i])
                if n2 - n1 != 1:
                    continue
                if isPred(j, i, wR):
                    cur = max(cur, dpR[j] + 1)
            dpR[i] = cur

        return max(dpR)
