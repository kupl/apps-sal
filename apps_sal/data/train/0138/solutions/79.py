class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        i_pos,i_neg=-1,len(nums)
        pro=1
        res=0
        for i in range(len(nums)):
            if nums[i]==0:
                i_pos,i_neg=i,len(nums)
                pro=1
            else: 
                if nums[i]<0: pro*=-1
      
                if pro>0:
                    i_pos=min(i,i_pos)
                    res=max(res,i-i_pos)
                else:
                    i_neg=min(i,i_neg)
                    res=max(res,i-i_neg)
        return res

