class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        even=0
        odd=0
        sum1=0
        result=0
        for num in arr:
            sum1+=num
            if sum1%2==0:
                result+=odd
                even+=1
            else:
                result+=even+1
                odd+=1
            result%=(10**9+7)
                
        return result
