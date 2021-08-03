class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        cur = res = 0
        seen = {}
        for i, h in enumerate(hours):
            cur += 1 if h > 8 else -1
            if cur > 0:
                res = max(res, i + 1)
            else:
                if cur - 1 in seen:
                    res = max(res, i - seen[cur - 1])
            if cur not in seen:
                seen[cur] = i

        return res
