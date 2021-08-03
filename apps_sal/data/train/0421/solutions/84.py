class Solution:
    def lastSubstring(self, s: str) -> str:
        max_idx = 0
        for i in range(1, len(s)):
            it = s[i]
            max_s = s[max_idx]
            if it >= max_s:
                j = 2
                while(it == max_s):
                    it = s[i:i + j]
                    max_s = s[max_idx:max_idx + j]
                    if i + j == len(s) + 1:
                        if it > max_s:
                            max_idx = i
                        return s[max_idx:]
                    j += 1
                if it > max_s:
                    max_idx = i

        return s[max_idx:]
