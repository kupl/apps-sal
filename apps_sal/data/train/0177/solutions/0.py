class Solution:

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        left = -1
        right = 0
        result = ''
        totalMatch = 0
        d = {}
        for c in t:
            d[c] = d.get(c, 0) + 1
        for right in range(len(s)):
            c = s[right]
            d[c] = d.get(c, 0) - 1
            if d[c] >= 0:
                totalMatch += 1
                if totalMatch == len(t):
                    totalMatch -= 1
                    left += 1
                    while d[s[left]] < 0:
                        d[s[left]] += 1
                        left += 1
                    d[s[left]] += 1
                    if result == '' or len(result) > right - left:
                        result = s[left:right + 1]
        return result
