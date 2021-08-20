"""
Using Rabin-Karp incremental hash
Reference:
https://leetcode.com/problems/longest-happy-prefix/discuss/547446/C%2B%2BJava-with-picture-incremental-hash-and-KMP
"""


class Solution:

    def longestPrefix(self, s: str) -> str:
        index = 0
        MOD = 10 ** 9 + 7
        mul = 1
        sLen = len(s)
        (prefixHash, suffixHash) = (0, 0)
        j = sLen - 1
        for i in range(sLen - 1):
            first = ord(s[i]) - ord('a')
            last = ord(s[j]) - ord('a')
            prefixHash = (prefixHash * 26 + first) % MOD
            suffixHash = (last * mul + suffixHash) % MOD
            mul = mul * 26 % MOD
            j -= 1
            if prefixHash == suffixHash:
                index = i + 1
        return s[:index]
