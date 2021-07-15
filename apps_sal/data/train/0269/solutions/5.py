class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        lis=[]
        for i in range(len(nums)):
            if nums[i]==1:
                lis.append(i)
        for i in range(1,len(lis)):
            if (lis[i]-lis[i-1])-1<k:
                return False
        return True
            

