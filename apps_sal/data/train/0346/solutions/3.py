class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix = {0: 1}
        count = 0
        result_count = 0
        for num in nums:
            if num % 2:
                count += 1
            prefix[count] = prefix.get(count, 0) + 1
            result_count += prefix.get(count - k, 0)
        return result_count
