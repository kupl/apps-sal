class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        # \"pos\", \"neg\" represent longest consecutive numbers ending with nums[i] forming a positive/negative product.
        nums.append(0)
        n = len(nums)
        pos, neg = 0, 0
        if nums[0] > 0: pos = 1
        if nums[0] < 0: neg = 1
        ans = pos
        for i in range(1, n):
            if nums[i] > 0:
                pos = 1 + pos
                neg = 1 + neg if neg > 0 else 0
            elif nums[i] < 0:
                pre_pos, pre_neg = pos, neg
                pos = 1 + pre_neg if pre_neg > 0 else 0
                neg = 1 + pre_pos
            else:
                pos, neg = 0, 0
            ans = max(ans, pos)
        return ans
    
        # nums.append(0)
        # start = -1
        # i = 0
        # firstn = -1
        # maxl = 0
        # nneg = 0
        # while i<len(nums):
        #     if nums[i]<0:
        #         nneg += 1
        #         if firstn<0: firstn = i
        #         lastn = i
        #     elif nums[i] == 0:
        #         if nneg%2 == 0:
        #             maxl = max(maxl,i-start-1)
        #         else:
        #             maxl = max([maxl,lastn-start-1,i-firstn-1])
        #         start = i
        #         nneg = 0
        #         firstn = -1
        #     i += 1
        # return maxl

