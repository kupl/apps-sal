class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        diff = []
        for i in range(len(s)):
            diff.append(abs(ord(s[i]) - ord(t[i])))

        i = 0
        ans = 0

        curr = 0
        for j in range(0, len(s)):
            curr = curr + diff[j]
            if curr <= maxCost:
                ans = max(ans, j - i + 1)
            else:
                curr = curr - diff[i]
                i = i + 1
        return ans
