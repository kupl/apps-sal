class Solution:
    def maxScore(self, points: List[int], num_cards: int) -> int:
        size = len(points) - num_cards
        min_subarray_sum = math.inf
        left = curr = 0
        for right, val in enumerate(points):
            curr += val
            if right - left + 1 > size:
                curr -= points[left]
                left += 1
            if right - left + 1 == size:
                min_subarray_sum = min(min_subarray_sum, curr)
        return sum(points) - min_subarray_sum
