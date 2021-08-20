class Solution:

    def longestPrefix(self, s: str) -> str:
        n = len(s)
        i = 0
        maxi = ''
        while i < n:
            print()
            if s[:i] == s[n - i:]:
                maxi = max(maxi, s[:i])
            i += 1
        print('maxi', maxi)
        return maxi
