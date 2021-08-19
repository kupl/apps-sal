class Solution:

    def canConvertString(self, s: str, t: str, k: int) -> bool:
        (n1, n2) = (len(s), len(t))
        if n1 != n2:
            return False
        if k == 0:
            return s == t
        steps = collections.defaultdict(int)
        for (sc, tc) in zip(s, t):
            if sc != tc:
                idx_t = ord(tc)
                idx_s = ord(sc)
                if idx_s < idx_t:
                    step = idx_t - idx_s
                else:
                    step = idx_t - idx_s + 26
                if step > k:
                    return False
                steps[step] += 1
        for step in steps:
            if (steps[step] - 1) * 26 + step > k:
                return False
        return True
