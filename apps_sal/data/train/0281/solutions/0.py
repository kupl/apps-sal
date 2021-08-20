class Solution:

    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        c = Counter(((ord(c2) - ord(c1)) % 26 for (c1, c2) in zip(s, t)))
        return k >= max((m + 26 * (count - 1) for (m, count) in list(c.items()) if m), default=0)
