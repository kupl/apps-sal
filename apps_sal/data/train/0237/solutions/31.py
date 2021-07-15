class Solution:
    def numSubarraysWithSum(self, nums: List[int], k: int) -> int:
        if not nums:    return 0

        counter = collections.defaultdict(int)
        counter[0] = 1
        cumsum = 0
        ans = 0
        for i in range(len(nums)):
            cumsum += nums[i]
            if cumsum-k in counter:
                ans += counter[cumsum-k]
            counter[cumsum] += 1
        return ans
