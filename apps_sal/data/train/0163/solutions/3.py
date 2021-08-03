class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        index = 0
        ans = True
        for i in s:
            if i not in t[index:]:
                ans = False
                break
            else:
                index += t[index:].index(i) + 1
        return ans
