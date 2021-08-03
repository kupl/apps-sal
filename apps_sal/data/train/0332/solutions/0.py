class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        left, right = 0, 0
        while left < len(s):
            while right < len(s) and s[right] == s[left]:
                right += 1
            ret += self.sum(right - left)
            l, r = left - 1, right
            while l >= 0 and r < len(s) and s[r] == s[l]:
                ret += 1
                l -= 1
                r += 1
            left = right
        return ret

    def sum(self, n):
        s = 0
        for i in range(1, n + 1):
            s += i
        return s
