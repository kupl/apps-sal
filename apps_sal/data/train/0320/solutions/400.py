class Solution:
    def minOperations(self, nums: List[int]) -> int:
        high=len(bin(max(nums)))-3
        one=sum([bin(n).count('1') for n in nums])
        return high+one
        

