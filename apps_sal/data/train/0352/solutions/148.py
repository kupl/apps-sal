class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        lis = [1 for _ in range(n)]

        def cmp(w1, w2):
            for k in range(len(w1)):
                if w1[0:k] + w1[k + 1:] == w2:
                    return True
            return False
        words = sorted(words, key=len)
        for i in range(1, n):
            for j in range(i):
                (l1, l2) = (len(words[j]), len(words[i]))
                if l1 == l2 - 1:
                    if cmp(words[i], words[j]):
                        if lis[i] < lis[j] + 1:
                            lis[i] = lis[j] + 1
        return max(lis)
