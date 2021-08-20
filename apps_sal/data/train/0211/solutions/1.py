class Solution:

    def maxUniqueSplit(self, s: str) -> int:
        start = 0
        end = 0
        se = set()
        res = 0

        def helper(stn, se, count):
            nonlocal res
            if not stn:
                res = max(res, count)
            if len(stn) + count <= res:
                return
            for i in range(1, len(stn) + 1):
                if stn[:i] not in se:
                    helper(stn[i:], se | {stn[:i]}, count + 1)
        helper(s, se, 0)
        return res
