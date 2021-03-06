class Solution:

    def longestWPI(self, hours: List[int]) -> int:
        s = 0
        seen = {}
        ans = 0
        for (i, h) in enumerate(hours):
            if h > 8:
                s += 1
            else:
                s -= 1
            if s > 0:
                ans = i + 1
            seen.setdefault(s, i)
            if s - 1 in seen:
                ans = max(ans, i - seen[s - 1])
        return ans
