class Solution:

    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        i = 0
        ans = 0
        curr = 0
        for j in range(0, len(s)):
            curr = curr + abs(ord(s[j]) - ord(t[j]))
            if curr <= maxCost:
                ans = max(ans, j - i + 1)
            else:
                curr = curr - abs(ord(s[i]) - ord(t[i]))
                i = i + 1
        print()
        return ans
