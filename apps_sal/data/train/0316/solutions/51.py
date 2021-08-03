MOD = 100000007


class Solution:
    def longestPrefix(self, s: str) -> str:

        r = 0

        L = R = 0
        multi = 1
        for i in range(len(s) - 1):
            L = (26 * L + ord(s[i]) - ord('a')) % MOD
            R = ((ord(s[~i]) - ord('a')) * multi + R) % MOD
            multi = multi * 26 % MOD
            if L == R:
                r = i + 1

        return s[:r]
