class Solution:

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        record = {}
        result = 0
        start = -1
        for (i, x) in enumerate(s):
            if x in record:
                start = max(start, record[x])
            record[x] = i
            result = max(result, i - start)
        return result
