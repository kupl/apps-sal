class Solution:
    def lastSubstring(self, s: str) -> str:
        left, right, length = 0, 1, 0
        n = len(s)
        while right + length < n:
            if s[left + length] == s[right + length]:
                length += 1
            elif s[left + length] > s[right + length]:
                right += length + 1
                length = 0
            else:
                left += length + 1

                right = left + 1
                length = 0

        return s[left:]
