class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        if len(s) == 0:
            return result

        hashmap = {}
        start = 0
        for i in range(len(s)):
            if s[i] in hashmap:
                start = max(hashmap[s[i]] + 1, start)
            hashmap[s[i]] = i
            result = max(result, i - start + 1)
        return result
