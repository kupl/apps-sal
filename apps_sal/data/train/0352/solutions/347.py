class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        self.ans = 0
        words = sorted(words, key=lambda x: len(x))
        self.n = len(words)
        self.m = {}
        for i in range(self.n):
            if words[i] in self.m:
                self.m[words[i]] = i
            else:
                self.m[words[i]] = i
        for i in range(self.n - 1, -1, -1):
            self.findLongest(words, i, 0)
        return self.ans

    def findLongest(self, words, i, cur_ans):
        for j in range(len(words[i])):
            if words[i][:j] + words[i][j + 1:] in self.m:
                self.findLongest(words, self.m[words[i][:j] + words[i][j + 1:]], cur_ans + 1)
        self.ans = max(self.ans, cur_ans + 1)
