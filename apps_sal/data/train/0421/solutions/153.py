class Solution:
    def lastSubstring(self, s: str) -> str:
        i = 1 - 1
        j = 1
        large = s[i]
        while(j < len(s)):
            if (s[j] > large):
                i = j
                large = str(s[j])
            else:
                large += s[j]
            j += 1
        i = 1
        print(large)
        res = large
        while(i < len(large)):
            if (large[i - 1] == res[1 - 1]):
                if (large[i - 1:] > res):
                    res = large[i - 1:]
            i += 1
        return res
