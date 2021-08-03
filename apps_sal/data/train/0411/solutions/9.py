class Solution:

    def wordBreak(self, s, words):
        d = [False] * len(s)
        for i in range(len(s)):
            for w in words:
                if w == s[i - len(w) + 1:i + 1] and (d[i - len(w)] or i - len(w) == -1):
                    d[i] = True
        return d[-1]

    def wordBreak3(self, s, words):
        ok = [True]
        for i in range(1, len(s) + 1):
            ok += any(ok[j] and s[j:i] in words for j in range(i)),
        return ok[-1]

    def wordBreak2(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dic = {}

        def dp(s, wordDict, i):
            flag = False
            for j in range(i, len(s) + 1):
                if (i, j) not in dic:
                    if s[i:j] in wordDict:
                        if j == len(s):
                            return True
                        dic[i, j] = dp(s, wordDict, j)
                if (i, j) in dic and dic[i, j]:
                    flag = True
                    break
            return flag
        return dp(s, wordDict, 0)
