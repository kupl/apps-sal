class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        s = 0
        fn = -1
        ln = -1
        cn = 0
        res = 0
        
        for i, v in enumerate(nums):
            if v == 0:
                end = i - 1
                if cn % 2 == 0:
                    res = max(res, end - s + 1)
                else:
                    res = max(res, end - fn, ln - s)
                s = i + 1
                fn = -1
                ln = -1
                cn = 0
            elif v < 0:
                if fn == -1:
                    fn = ln = i
                else:
                    ln = i
                cn += 1
        end = len(nums) - 1
        if cn % 2 == 0:
            res = max(res, end - s + 1)
        else:
            res = max(res, end - fn, ln - s)
        return res
