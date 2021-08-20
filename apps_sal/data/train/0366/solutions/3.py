class Solution:

    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        for i in set(s):
            if s.count(i) < k:
                return max((self.longestSubstring(t, k) for t in s.split(i)))
        return len(s)
