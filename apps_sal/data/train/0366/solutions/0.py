class Solution:

    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        for c in set(s):
            if s.count(c) < k:
                return max((self.longestSubstring(sp, k) for sp in s.split(c)))
        return len(s)
