class Solution:
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
            hash2 = (hash2 + mul * (ord(s[j]) - ord('a'))) % mod
            mul = mul * 26 % mod
            if hash1 == hash2:
                res = i + 1
            i += 1
            j -= 1
        return s[:res]
