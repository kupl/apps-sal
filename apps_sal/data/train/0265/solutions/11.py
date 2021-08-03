

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
class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        
        prefixsum = {}
        prefixsum[0] = 0
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
