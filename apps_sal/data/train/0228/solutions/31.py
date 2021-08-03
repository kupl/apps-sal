class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        i = 0
        j = i + k - 1
        cc = 0
        for k in range(i, j + 1):
            if s[k] == 'a' or s[k] == 'e' or s[k] == 'i' or s[k] == 'o' or s[k] == 'u':
                cc += 1

        max_c = 0
        while j < len(s):
            if cc > max_c:
                max_c = cc
            if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
                cc -= 1
            i += 1
            j += 1
            if j < len(s):
                if s[j] == 'a' or s[j] == 'e' or s[j] == 'i' or s[j] == 'o' or s[j] == 'u':
                    cc += 1

        return max_c
