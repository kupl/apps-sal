class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        res = 0
        dic = collections.defaultdict(int)
        words.sort(key=lambda x: len(x))
        for w in words:
            m = len(w)
            for i in range(m):
                new = w[:i] + w[i + 1:]
                dic[w] = max(dic[w], dic[new] + 1)
            res = max(res, dic[w])
        return res
