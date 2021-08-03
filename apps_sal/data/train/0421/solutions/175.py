class Solution:
    def lastSubstring(self, s: str) -> str:
        s_len, left, right, step = len(s), 0, 1, 0
        while(right + step < s_len):
            if s[right + step] > s[left + step]:
                left, right, step = right, right + 1, 0
            elif s[right + step] < s[left + step]:
                right, step = right + step + 1, 0
            else:
                step += 1
        return s[left:]
