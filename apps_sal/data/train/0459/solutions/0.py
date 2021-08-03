class Solution:
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if s == "":
            return 0
        count = {}
        lo = 0
        hi = 0
        max_letter = 0
        for hi in range(len(s)):
            try:
                count[s[hi]] += 1
            except:
                count[s[hi]] = 1
            if count[s[hi]] > max_letter:
                max_letter = count[s[hi]]
            if max_letter < hi - lo + 1 - k:
                if max_letter == count[s[lo]]:
                    max_letter -= 1
                count[s[lo]] -= 1
                lo += 1
        return hi - lo + 1
