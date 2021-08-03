class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        max_seen = max(A)
        if max_seen < 0:
            return max_seen
        min_seen = float('inf')
        curr_max = 0
        curr_min = 0
        total = 0

        for num in A:
            total += num
            curr_max = max(0, curr_max + num)
            curr_min = min(0, curr_min + num)
            max_seen = max(max_seen, curr_max)
            min_seen = min(min_seen, curr_min)

        return max(max_seen, total - min_seen)
