from collections import Counter


class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        lookup = Counter()
        lookup[0] = 1
        answer = accumulated_sum = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                accumulated_sum += 1
            answer += lookup[accumulated_sum - k]
            lookup[accumulated_sum] += 1
        return answer
