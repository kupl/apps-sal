class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:

        if len(s) != len(t):
            return False

        diff = defaultdict(int)
        for sc, tc in zip(s, t):
            d = (ord(tc) - ord(sc)) % 26
            if d == 0:
                continue
            if d > k:
                return False
            diff[d] += 1
            if ((diff[d] - 1) * 26) + d > k:
                return False

        return True
