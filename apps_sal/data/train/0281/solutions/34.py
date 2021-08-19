class Solution:

    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        dd = collections.defaultdict(int)
        for (i, v) in zip(s, t):
            diff = (ord(v) - ord(i)) % 26
            if diff > 0 and diff + dd[diff] * 26 > k:
                return False
            dd[diff] += 1
        return True
