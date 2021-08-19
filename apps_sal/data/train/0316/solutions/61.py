class Solution:
    # kmp, time: O(n), space: O(n)
    # build the LPS table; lps: longest proper prefix which is also suffix.
    # lps[i]: for pattern[:i], the longest prefix which is a also the suffix
    def build(self, p):
        leng = 0
        i = 1
        lps = [0]
        while i < len(p):
            if p[i] == p[leng]:
                i += 1
                leng += 1
                lps.append(leng)
            else:
                if leng:
                    leng = lps[leng - 1]
                else:
                    lps.append(0)
                    i += 1
        return lps

    def longestPrefix2(self, s: str) -> str:
        lps = self.build(s)
        return s[:lps[-1]]

    # rolling hash
    # for the string of i size, the hash is: s[0] * 26 ^ (i - 1) + s[1] * 26 ^ (i -2) + ... + s[i - 2] * 26 + s[i - 1].

    def longestPrefix(self, s: str) -> str:
        mul = 1
        mod = pow(10, 9) + 7
        i = 0
        j = len(s) - 1
        res = 0
        hash1 = 0
        hash2 = 0
        while i < len(s) - 1 and j > 0:
            hash1 = (hash1 * 26 + ord(s[i]) - ord('a')) % mod
            # s[n-1] -> s[n-2]*26 + s[n-1] -> s[n-3]*26^2 + s[n-2]*26 + s[n-1]
            hash2 = (hash2 + mul * (ord(s[j]) - ord('a'))) % mod
            mul = mul * 26 % mod
            if hash1 == hash2:
                res = i + 1
            i += 1
            j -= 1
        return s[:res]
