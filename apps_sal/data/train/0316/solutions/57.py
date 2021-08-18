class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return ''

        prefix, suffix, base = 0, 0, 1
        NUM = 10**9 + 7
        ans = ''
        for i in range(1, n):
            x = ord(s[i - 1]) - ord('a')
            prefix = (26 * prefix + x) % NUM

            x = ord(s[n - i]) - ord('a')
            suffix = (suffix + x * base) % NUM
            base = (base * 26) % NUM

            if prefix == suffix:
                if s[0:i] == s[n - i:n]:
                    ans = s[0:i]
        return ans
