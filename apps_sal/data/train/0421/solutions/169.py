class Solution:

    def lastSubstring(self, s: str) -> str:
        n = len(s)
        i = n - 2
        last = n - 1
        while i >= 0:
            if s[i] > s[last]:
                last = i
                i -= 1
                continue
            if s[i] < s[last]:
                i -= 1
                continue
            j = 1
            while True:
                tempi = i + j
                templast = last + j
                if templast >= n:
                    last = i
                    i -= 1
                    break
                if tempi == last:
                    last = i
                    i -= 1
                    break
                if s[tempi] > s[templast]:
                    last = i
                    i -= 1
                    break
                if s[tempi] < s[templast]:
                    i -= 1
                    break
                j += 1
        return s[last:]
