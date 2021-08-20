class Solution:

    def findTheLongestSubstring(self, s: str) -> int:
        P = [0]
        vowels = 'aeiou'
        for c in s:
            i = vowels.find(c)
            mask = 1 << i if i != -1 else 0
            P.append(P[-1] ^ mask)
        ans = 0
        fst = {}
        for (i, p) in enumerate(P):
            if p in fst:
                h = fst[p]
                ans = max(ans, i - h)
            fst.setdefault(p, i)
        return ans
