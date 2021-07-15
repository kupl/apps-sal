class Solution:
    
    def __init__(self):
        self.all_pos_array = []
    
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        while len(self.all_pos_array) < right:
            for i in range(0,len(nums)):
                for j in range(i,len(nums)):
                    self.all_pos_array.append(sum(nums[i:j+1]))
        
        return sum(sorted(self.all_pos_array)[left-1:right]) % (10**9 +7)

