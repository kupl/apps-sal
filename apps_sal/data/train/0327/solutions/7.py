class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        idx = i = 0
        record = set()
        count = 0
        maxcount = 0
        while i < len(s):
            if s[i] in record:
                record.remove(s[idx])
                count -= 1
                idx += 1
            else:
                record.add(s[i])
                count += 1
                i += 1
                if count > maxcount:
                    maxcount = count

        return maxcount
