class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        st = set(words)

        def ls(word):
            res = 1
            for j in range(len(word)):
                substr = word[:j] + word[(j+1):]
                if substr not in st:
                    continue
                res = max(res, 1 + ls(substr))
            return res
           
        res = 1
        for word in words:
            res = max(res, ls(word))
        return res
