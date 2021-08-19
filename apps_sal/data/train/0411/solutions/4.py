class Solution:

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        ok = [True]
        for i in range(1, len(s) + 1):
            ok += (any((ok[j] and s[j:i] in wordDict for j in range(i))),)
            print(ok)
        return ok[-1]
