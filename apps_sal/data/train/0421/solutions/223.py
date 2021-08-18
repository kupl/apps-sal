class Solution:
    def lastSubstring(self, s: str) -> str:
        max_idx = 0
        curr_idx = 1
        while curr_idx <= len(s) - 1:
            step = 0
            while curr_idx + step <= len(s) - 1 and s[curr_idx + step] == s[max_idx + step]:
                step += 1

            if curr_idx + step == len(s):
                break

            if s[curr_idx + step] > s[max_idx + step]:
                max_idx = curr_idx
                curr_idx = curr_idx + 1
            else:
                curr_idx = curr_idx + step + 1
        return s[max_idx:]
