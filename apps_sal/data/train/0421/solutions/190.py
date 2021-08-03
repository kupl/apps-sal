class Solution:
    def lastSubstring(self, s: str) -> str:
        maxStr = s
        for i in range(1, len(s)):
            if s[i:] > maxStr:
                maxStr = s[i:]

        return maxStr
