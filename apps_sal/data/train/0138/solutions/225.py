class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        listt = []
        a = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                listt.append(nums[a + 1:i])
                a = i
        listt.append(nums[a + 1:])
        while [] in listt:
            listt.remove([])
        if listt == []:
            return 0
        recordlist = {}
        for i in range(len(listt)):
            firstneg = -1
            begneg = -1
            recordlist[i] = 0
            for m in range(len(listt[i])):
                if listt[i][m] < 0 and firstneg == -1:
                    firstneg = m
                    if begneg == -1:
                        begneg = m
                    continue
                if listt[i][m] < 0 and firstneg != -1:
                    firstneg = -1
            if firstneg == -1:
                recordlist[i] = len(listt[i])
            else:
                recordlist[i] = max([firstneg, len(listt[i]) - firstneg - 1, begneg, len(listt[i]) - begneg - 1])
        m = []
        for i in list(recordlist.values()):
            m.append(i)
        return max(m)
