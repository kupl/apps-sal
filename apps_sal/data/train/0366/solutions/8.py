class Solution:

    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        s_set = set(s)
        ans = -2147483647
        for c in s_set:
            if s.count(c) < k:
                return max([self.longestSubstring(_s, k) for _s in s.split(c)])
        return len(s)
