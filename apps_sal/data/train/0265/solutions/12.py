### good explanation in https://www.youtube.com/watch?v=EW521e8c8lk

### video starts 10:40

class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:

        prefixsum = {}
        prefixsum[0] = True
        prev = 0
        res = 0
        for num in nums:
            curr = prev + num
            
            if curr - target in prefixsum:
                res += 1
                prefixsum = {}
                prefixsum[0] = True
                prev = 0
            
            else:
                prefixsum[curr] = True
                prev = curr
            
        print(res)
        return res
        
        
        
        



'''
It seems that I have exact the same idea as the following post
https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/discuss/780882/Java-14-lines-Greedy-PrefixSum-with-line-by-line-explanation-easy-to-understand

why does the following code now working???? 


### The following code does not pass submission ..... 
class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        
        prefixsum = {}
        prefixsum[0] = -1
        res = 0
        last = -1
        prev = 0
        for idx, num in enumerate(nums):
            curr = prev + num
            prefixsum[curr] = idx
            
            if curr - target in prefixsum:
                if prefixsum[curr - target] >= last:
                    res += 1
                    last = prefixsum[curr]
            prev = curr 
        print(prefixsum)
        print(res)
        return res


'''





