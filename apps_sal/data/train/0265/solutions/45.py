class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        n = len(nums)
        hashmap = {0: 0}
        ans = 0
        sums = 0
        for i in range(n):
            sums += nums[i]
            if sums - target in hashmap:
                ans = max(ans, hashmap[sums - target] + 1)
            hashmap[sums] = ans
        return ans
