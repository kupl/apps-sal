class Solution:

    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        end = 0
        result = 0
        allCost = 0
        for start in range(len(s)):
            if start >= 1:
                allCost -= abs(ord(s[start - 1]) - ord(t[start - 1]))
            while end + 1 < len(s) + 1 and allCost + abs(ord(s[end]) - ord(t[end])) <= maxCost:
                end += 1
                allCost += abs(ord(s[end - 1]) - ord(t[end - 1]))
            result = max(result, end - start)
        return result
