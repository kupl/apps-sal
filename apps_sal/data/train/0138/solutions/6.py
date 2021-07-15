class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n=len(nums)
        pos,neg=0,0
        [0,1,-2,-3,-4]
        if nums[0]>0:
            pos=1
        if nums[0]<0:
            neg=1
        ans=pos
        for i in range(1,n):
            if nums[i]>0:
                pos = 1 + pos
                neg = 1 + neg if neg >0 else 0
            elif nums[i]<0:
                pre_pos,pre_neg=pos,neg
                pos= 1 + pre_neg if pre_neg >0 else 0
                neg = 1 + pre_pos
            else:
                pos,neg =0,0
            ans = max(ans,pos)
        return ans
