class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        r = 0
        c = collections.Counter()
        countToNums = collections.Counter()
        high = 0
        unique = 0
        
        for i in range(len(nums)):
            if not c[nums[i]]:
                unique += 1
            
            countToNums[c[nums[i]]] -= 1
            c[nums[i]] += 1
            countToNums[c[nums[i]]] += 1
            if c[nums[i]] > high:
                high = c[nums[i]]
                
            if countToNums[high] == 1 and countToNums[high-1] == unique-1 or countToNums[1] == 1 and countToNums[high] == unique-1 or high == 1:
                r = i+1
                
        return r
            

