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
        # print(num)
        mask = (1 << (k - 1)) - 1
        # print(mask)
        for i in range(k, len(s)):
            num &= mask
            m = ord(s[i]) - ord('0')
            num = num * 2 + m
            d.add(num)
        # print(len(d))
        return len(d) >= (1 << k)
