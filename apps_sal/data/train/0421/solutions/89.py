class Solution:

    def lastSubstring(self, s: str) -> str:
        (left, right) = (0, 0)
        while right < len(s):
            if s[right] > s[left]:
                left = right
            elif s[right] == s[left]:
                if s[left:right] < s[right:right + right - left]:
                    left = right
            right += 1
        return s[left:right + 1]
