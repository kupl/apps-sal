class Solution:

    def lastSubstring(self, s: str) -> str:
        begin = 0
        end = 1
        offset = 0
        while end + offset < len(s):
            if s[begin + offset] > s[end + offset]:
                offset = 0
                end += 1
            elif s[begin + offset] < s[end + offset]:
                begin = end
                end += 1
                offset = 0
            else:
                offset += 1
        return s[begin:]
