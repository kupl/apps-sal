class Solution:
    def longestPrefix(self, s: str) -> str:
        ans = ''
        l, r = 0, 0
        mod = 10**9 + 7
        for i in range(len(s) - 1):
            l = (l * 31 + ord(s[i])) % mod
            r = (r + ord(s[len(s) - i - 1]) * pow(31, i, mod)) % mod
            if l == r and s[: i + 1] == s[len(s) - i - 1:]:
                ans = s[:i + 1]
        return ans
