class Solution:

    def getMaxLen(self, nums: List[int]) -> int:

        def oddMinus(ls):
            ret = 0
            for i in range(len(ls)):
                if ls[i] < 0:
                    ret = max(max(ret, i), len(ls) - 1 - i)
            return ret

        def getLen(ls):
            minus = 0
            for i in ls:
                if i < 0:
                    minus += 1
            if minus % 2 == 0:
                return len(ls)
            else:
                return oddMinus(ls)
        s = []
        sub = []
        for i in nums:
            if i == 0:
                s.append(sub)
                sub = []
            else:
                sub.append(i)
        s.append(sub)
        res = 0
        for ls in s:
            res = max(res, getLen(ls))
        return res
