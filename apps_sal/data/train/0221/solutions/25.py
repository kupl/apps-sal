class Solution:
    def longestDupSubstring(self, S: str) -> str:
        p = 239017
        pows = [[1], [1]]
        hsh = [[0], [0]]
        mods = [int(1e9) + 7, int(1e9) + 9]
        for ch in S:
            for i in range(len(mods)):
                hsh[i].append((hsh[i][-1] + ord(ch) * pows[i][-1]) % mods[i])
                pows[i].append((pows[i][-1] * p) % mods[i])
        l = 0
        r = len(S)
        substrs = {}
        ans = ''
        while r - l > 1:
            m = (r + l) // 2
            found = False
            for i in range(0, len(S) - m + 1):
                h0 = ((hsh[0][i + m] - hsh[0][i]) * pows[0][-(i + 1)]) % mods[0]
                h1 = ((hsh[1][i + m] - hsh[1][i]) * pows[1][-(i + 1)]) % mods[1]
                if (h0, h1) in substrs:
                    found = True
                    ans = S[i: i + m]
                    break
                else:
                    substrs[(h0, h1)] = True
            if found:
                l = m
            else:
                r = m
            substrs.clear()
        return ans
