class Solution:

    def longestWPI(self, hours: List[int]) -> int:
        hours = [1 if h > 8 else -1 for h in hours]
        seen = {}
        ans = cur = 0
        for (i, h) in enumerate(hours):
            cur += h
            seen.setdefault(cur, i)
            if cur > 0:
                ans = i + 1
            elif cur - 1 in seen:
                ans = max(ans, i - seen[cur - 1])
        return ans
