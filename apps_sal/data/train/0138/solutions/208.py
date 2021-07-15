class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        start, curnegcnt, res, fnegpos, lnegpos = 0, 0, 0, 0, 0
        flag = True
        i, j = 0, len(nums)
        while i < j:
            if nums[i] == 0:
                flag = True
                i += 1
                start = i
                curnegcnt = 0
                continue
            if nums[i] < 0:
                if flag:
                    flag = False
                    fnegpos = i
                lnegpos = i
                curnegcnt += 1
            if curnegcnt == 0 or curnegcnt % 2 == 0:
                res = max(res, (i - start) + 1)
            else:

                res = max(res, (lnegpos ) - start, i - (fnegpos ))
            i += 1
        return res
                
                
    

