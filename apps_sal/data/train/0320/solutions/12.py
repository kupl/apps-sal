import collections

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        sum = 0
        for num in nums:
            sum += collections.Counter(bin(num))['1']
            
        sum += len(bin(max(nums))) - 3
        return sum

