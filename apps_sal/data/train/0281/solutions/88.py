class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        n = len(s)
        g = [0 for i in range(26)]
        for i in range(n):
            g[(ord(t[i]) - ord(s[i])) % 26] += 1
        for i in range(1, 26):
            index = i + (g[i]-1) * 26
            if index > k:
                return False
        return True
