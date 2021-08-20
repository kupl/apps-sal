class Solution:

    def canConvertString(self, s: str, t: str, k: int) -> bool:
        times = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            orig = (ord(t[i]) - ord(s[i]) + 26) % 26
            totry = orig
            if totry == 0:
                continue
            if orig in times:
                totry = times[orig]
                totry += 26
            if totry > k:
                return False
            times[orig] = totry
        return True
