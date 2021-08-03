class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        d = collections.defaultdict(list)
        for word in words:
            d[len(word)].append(word)

        lengths = sorted(list(d.keys()))
        self.mem = {}

        def dfs(word):
            if len(word) == lengths[-1]:
                return 1
            if word in self.mem:
                return self.mem[word]

            nxt_length = 0
            for nxt_word in d[len(word) + 1]:
                for j in range(len(nxt_word)):
                    if word == nxt_word[:j] + nxt_word[j + 1:]:
                        nxt_length = max(nxt_length, dfs(nxt_word))

            self.mem[word] = nxt_length + 1
            return nxt_length + 1

        res = 0
        for word in words:
            res = max(res, dfs(word))

        return res
