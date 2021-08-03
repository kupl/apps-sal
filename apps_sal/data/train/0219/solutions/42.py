class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        total = res = 0
        index = {}
        for i, h in enumerate(hours):
            total += 1 if h > 8 else -1
            if total > 0:
                res = i + 1
            if total - 1 in index:
                res = max(res, i - index[total - 1])
            index.setdefault(total, i)

        return res
