class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        non_zeros = []
        i = 0
        pre = 0
        while i < n:
            if nums[i] == 0:
                if i > pre:
                    non_zeros.append(nums[pre:i])
                pre = i + 1
            i += 1
        if i > pre:
            non_zeros.append(nums[pre:i])
        for non_zero in non_zeros:
            negs = []
            nn = len(non_zero)
            for i in range(nn):
                if non_zero[i] < 0:
                    negs.append(i)
            if len(negs) % 2 == 0:
                res = max(res, nn)
            else:
                res = max([res, len(non_zero[negs[0] + 1:nn]), len(non_zero[0:negs[-1]])])
        return res
