class Solution:

    def lastSubstring(self, s: str) -> str:
        n = len(s)
        max_char = max(s)
        max_index = None
        for (i, x) in enumerate(s):
            if x == max_char:
                if max_index is None:
                    max_index = i
                elif i > 0 and s[i - 1] != max_char:
                    cand1 = max_index + 1
                    cand2 = i + 1
                    while cand2 < n and s[cand1] == s[cand2]:
                        cand1 += 1
                        cand2 += 1
                    if cand2 == n:
                        continue
                    if s[cand1] < s[cand2]:
                        max_index = i
        return s[max_index:]
