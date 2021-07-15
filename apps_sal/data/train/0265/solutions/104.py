class Solution:
    
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        
        if len(nums) == 0:
            return 0
        result = 0
        
        # target = 10
        # [-2,6, 6, 3, 5, 4, 1, 2, 8]
        # [-2,4,10,13,18,22,23,25,33]
        #                         ^
        # seen: [0]
        # result = 2
        
        prefixSums = []
        partial = 0
        
        seen = set([0])
        
        for i in range(len(nums)):
            partial += nums[i]
            prefixSums.append(partial)
            required = prefixSums[i] - target
            if required in seen:
                result += 1
                seen = set()
            seen.add(prefixSums[i])
            
        return result
        
        

