class Solution:

    def lastSubstring(self, s: str) -> str:
        left = 0
        right = 1
        step = 0
        while right + step < len(s):
            if s[left + step] < s[right + step]:
                left = right
                right += 1
                step = 0
            elif s[left + step] == s[right + step]:
                step += 1
            else:
                right += step + 1
                step = 0
        return s[left:]
