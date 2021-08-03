class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        cum_sum = [0]
        for number in nums:
            cum_sum.append((cum_sum[-1] + number) % p)
        overall_sum = cum_sum[-1]
        if overall_sum % p == 0:
            return 0
        self.memory = {}
        longest_dist = len(nums) + 5
        for j, cur_sum in enumerate(cum_sum[:-1]):
            if cur_sum % p == 0:
                longest_dist = min(longest_dist, len(cum_sum) - j - 1)
            if (overall_sum - cur_sum) % p in self.memory:
                i = self.memory[(overall_sum - cur_sum) % p]
                longest_dist = min(longest_dist, j - i)
            self.memory[(- cur_sum) % p] = j

        if longest_dist >= len(nums):
            return -1
        return longest_dist
