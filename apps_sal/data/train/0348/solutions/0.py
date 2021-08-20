import sys


class Solution:

    def maximumSum(self, arr: List[int]) -> int:
        ignore = 0
        not_ignore = 0
        res = -sys.maxsize
        for i in arr:
            if i >= 0:
                ignore += i
                not_ignore += i
            else:
                if ignore == 0:
                    ignore += i
                else:
                    ignore = max(ignore + i, not_ignore)
                not_ignore += i
            res = max(res, ignore)
            if ignore < 0:
                ignore = 0
            if not_ignore < 0:
                not_ignore = 0
        return res
