class Solution:

    def lastSubstring(self, s: str) -> str:
        i = 0
        j = i + 1
        result = s
        while j < len(s):
            if s[i] > s[j]:
                j += 1
                continue
            elif s[i] < s[j]:
                i = j
                j += 1
            else:
                step = 0
                while j + step < len(s) and s[i + step] == s[j + step]:
                    step += 1
                if j + step == len(s):
                    return s[i:]
                if s[i + step] > s[j + step]:
                    j += 1
                    continue
                else:
                    i = j
                    j += 1
        return s[i:]
