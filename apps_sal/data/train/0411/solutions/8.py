class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        words = {w for w in wordDict}
        n = len(s) + 1
        ok = [False] * n
        ok[0] = True
        for j in range(1, n):
            for i in range(j):
                if ok[i] and s[i: j] in words:
                    ok[j] = True
                    break
        return ok[-1]
