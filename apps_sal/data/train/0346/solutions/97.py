from collections import Counter


class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        lookup = Counter()
        lookup[0] = 1
        answer = accumulated_odd = 0
        for num in nums:
            if num % 2 == 1:
                accumulated_odd += 1
            answer += lookup[accumulated_odd - k]
            lookup[accumulated_odd] += 1
        return answer
