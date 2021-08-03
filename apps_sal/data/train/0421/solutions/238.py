class Solution:
    def lastSubstring(self, s: str) -> str:
        n = len(s)
        left = 0
        right = 1
        step = 0

        while right + step < n:
            if s[right + step] > s[left + step]:
                left, right, step = right, right + 1, 0
            elif s[right + step] < s[left + step]:
                right, step = right + step + 1, 0
            else:
                step += 1

        return s[left:]
