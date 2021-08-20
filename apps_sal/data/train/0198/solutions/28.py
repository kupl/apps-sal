class Solution:

    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        start = 0
        end = 0
        cost = 0
        best = 0
        while end < len(s):
            while end < len(s) and cost + abs(ord(s[end]) - ord(t[end])) <= maxCost:
                cost += abs(ord(s[end]) - ord(t[end]))
                end += 1
            if start == end:
                start += 1
                end += 1
                continue
            best = max(best, end - start)
            cost -= abs(ord(s[start]) - ord(t[start]))
            start += 1
        return best
