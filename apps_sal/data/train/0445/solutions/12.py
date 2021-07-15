class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 5: return 0
        nums.sort()
        return min([ nums[n-4+i] - nums[i] for i in range(4)])
        
        #return min(a - b for a,b in zip(heapq.nlargest(4, A), heapq.nsmallest(4, A)[::-1]))

