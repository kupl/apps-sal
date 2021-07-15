class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        prefix = [0]*(len(nums)+1)
        counts = defaultdict(int)
        counts[0] = 1
        tot = 0
        for i in range(1,len(nums)+1):
            prefix[i] = nums[i-1] + prefix[i-1]
            if counts[prefix[i]-target] != 0:
                tot += 1
                counts = defaultdict(int)
                prefix[i] = 0
            counts[prefix[i]] += 1
        return tot

