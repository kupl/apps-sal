class Solution:
    # idea is we have two sequences: i ...i+k and j ...j+k and differ only at s[i+k] and j[i+k]
    def lastSubstring(self, s: str) -> str:
        i, j, k = 0, 1, 0
        while j + k < len(s):
            if s[i + k] == s[j + k]:
                k += 1
                continue
            elif s[i+k] > s[j+k]:
                # increase j value to get out of loop
                j = j + k + 1; 
            else: 
                # increase i value because we just found a starting letter that is bigger
                i = i + k +1; 
            if i == j: 
                j = j + 1 
            k = 0
        return s[i:]

