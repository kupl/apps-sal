class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        remain = total % p
        if remain == 0:
            return 0

        prefix_sum_dict = {0: -1}
        result = float('inf')
        curr_sum = 0
        for i, num in enumerate(nums):
            curr_sum = (curr_sum + num) % p
            prefix_sum_dict[curr_sum] = i

            target = (curr_sum - remain) % p
            if target in prefix_sum_dict:
                result = min(result, i - prefix_sum_dict[target])

        if result != float('inf') and result < len(nums):
            return result
        return -1
