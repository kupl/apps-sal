class Solution:
    
    def find(self, nums, div):
        ans = 0
        for i in nums:
            ans += i//div
            if i%div!=0:
                ans += 1
        return ans
    
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)
        while low<high:
            mid = (low+high)//2
            cur = self.find(nums, mid)
            if mid>1:
                prev = self.find(nums, mid-1)
            else:
                prev = 0
            if mid == 1 and cur<=threshold:
                return 1
            if cur<=threshold and prev>threshold:
                return mid
            elif cur>threshold:
                low = mid+1
            elif prev<=threshold:
                high = mid-1
        return (low+high)//2
