from collections import defaultdict
class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        cnt = defaultdict(int)
        res = 0
        for i in range(len(s)):
            j = (ord(t[i]) - ord(s[i]) + 26) % 26
            if j:
                res = max(res, 26 * cnt[j] + j)
                cnt[j] += 1
        return res <= k
