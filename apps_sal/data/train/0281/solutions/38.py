class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        jumps = list(range(26))
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] == t[i]:
                continue
            jump = (ord(t[i]) - ord(s[i]) + 26) % 26
            if jumps[jump] > k:
                return False
            jumps[jump] += 26
        return True
