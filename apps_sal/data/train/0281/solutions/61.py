from collections import Counter


class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        ans = Counter()
        for i in range(len(s)):
            key = (ord(t[i]) - ord(s[i])) % 26
            if key != 0 and ans[key] * 26 + key > k:
                return False
            ans[key] += 1
        return True
