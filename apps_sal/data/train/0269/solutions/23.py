class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        n=len(nums)
        prev=-1
        
        ans=[]
        for i in range(n):
            if prev==-1:
                if nums[i]==1:
                    prev=i
            else:
                if nums[i]==1:
                    ans.append(i-prev-1)
                    prev=i
            
        for i in ans:
            if i<k:
                return False
        return True
