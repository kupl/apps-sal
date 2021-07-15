class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        
        subsum = [x for x in nums]
        
        for i, num in enumerate(nums):
            
            temp = num
            for j, cur in enumerate(nums[i+1:]):
                temp += cur
                subsum.append(temp)
        
        subsum.sort()
        
        return sum(subsum[left-1:right]) % (10**9 +7)
