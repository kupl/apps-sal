class Solution:

    def hasAllCodes(self, s: str, k: int) -> bool:
        if k >= len(s):
            return False
        d = set()
        num = 0
        for i in range(k):
            m = ord(s[i]) - ord('0')
            num = num * 2 + m
        d.add(num)
        mask = (1 << k - 1) - 1
        for i in range(k, len(s)):
            num &= mask
            m = ord(s[i]) - ord('0')
            num = num * 2 + m
            d.add(num)
        return len(d) >= 1 << k
