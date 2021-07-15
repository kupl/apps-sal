class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        result= []
        n= len(nums)
        for i in range(n):
            if (nums[i]==1):
                result.append(i+1)
        m= len(result)
        for j in range(m-1):
            if (result[j+1]- result[j]) <= k:
                return False
                    
        return True
