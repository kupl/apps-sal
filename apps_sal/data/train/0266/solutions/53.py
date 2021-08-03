from collections import Counter


class Solution:
    def numSplits(self, s: str) -> int:
        c2nl = Counter('')
        c2nr = Counter(s)
        n = len(s)
        ans = 0
        for i in range(n - 1):
            c2nl[s[i]] += 1
            c2nr[s[i]] -= 1
            if c2nr[s[i]] == 0:
                del c2nr[s[i]]
            if len(c2nl) == len(c2nr):
                ans += 1
        return ans
