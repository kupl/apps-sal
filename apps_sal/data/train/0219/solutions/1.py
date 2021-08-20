class Solution:

    def longestWPI(self, hours: List[int]) -> int:
        (ans, cum, seen) = (0, 0, {})
        for (i, hour) in enumerate(hours):
            cum = cum + 1 if hour > 8 else cum - 1
            if cum > 0:
                ans = i + 1
            else:
                if cum not in seen:
                    seen[cum] = i
                if cum - 1 in seen:
                    ans = max(ans, i - seen[cum - 1])
        return ans
