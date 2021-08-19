from collections import Counter


class Solution:

    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        cnt = [0] * 26
        for (cs, ct) in zip(s, t):
            diff = (ord(ct) - ord(cs)) % 26
            if diff > 0 and cnt[diff] * 26 + diff > k:
                return False
            cnt[diff] += 1
        return True
