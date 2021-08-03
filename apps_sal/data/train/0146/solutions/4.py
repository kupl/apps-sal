class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ""
        idx = 0
        while s[idx].isdigit():
            idx += 1
        if idx > 0:
            k = int(s[:idx])
            idx += 1
            idx_from = idx
            bracket_count = 1
            while bracket_count > 0:
                if s[idx] == "[":
                    bracket_count += 1
                elif s[idx] == "]":
                    bracket_count -= 1
                idx += 1
            return self.decodeString(s[idx_from:idx - 1]) * k + self.decodeString(s[idx:])
        return s[0] + self.decodeString(s[1:])
