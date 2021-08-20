class Solution:

    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        taken = [i for i in range(0, 26)]
        for (c1, c2) in zip(s, t):
            g = (ord(c2) - ord(c1)) % 26
            if g == 0:
                continue
            if taken[g] > k:
                return False
            taken[g] += 26
        return True
