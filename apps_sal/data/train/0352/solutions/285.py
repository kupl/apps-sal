class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        dic = collections.Counter()
        res = 0
        for word in words:
            for i in range(len(word)):
                pre = word[:i] + word[i + 1:]
                dic[word] = max(dic[word], dic[pre] + 1)
            res = max(res, dic[word])
        return res
