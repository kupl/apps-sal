class Solution:

    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        d = {x: 0 for x in range(1, 26)}
        for (cs, ct) in zip(s, t):
            diff = (ord(ct) - ord(cs) + 26) % 26
            if diff == 0:
                continue
            nxt = d[diff] * 26 + diff
            if nxt <= k:
                d[diff] += 1
            else:
                return False
        return True
