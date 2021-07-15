class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        listx=[]
        for i in range(0,len(nums)):
            if nums[i]==1:
                if listx:
                    if abs(i-listx[-1])>=k+1:
                        listx.append(i)
                    else:
                        return False
                else:
                    listx.append(i)
                    
        return True
