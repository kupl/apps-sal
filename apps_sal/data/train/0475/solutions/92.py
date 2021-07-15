class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        totalSums = []
        
        for i in range(len(nums)):
            curr = 0
            for j in range(i, len(nums)):
                curr += nums[j]
                totalSums.append(curr)
                
        totalSums.sort()
        
        return sum(totalSums[n] for n in range(left - 1, right)) % (10 ** 9 + 7)
