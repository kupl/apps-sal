class Solution:
    def maxScore(self, card_points: List[int], k: int) -> int:
        window_size = len(card_points) - k
        current_min_sum, min_sum = 0, sys.maxsize
        total_points = 0
        left = 0
        for right, value in enumerate(card_points):
            total_points += value
            current_min_sum += value

            current_size = right - left + 1
            if current_size < window_size:
                continue

            if current_size > window_size:
                current_min_sum -= card_points[left]
                left += 1

            min_sum = min(min_sum, current_min_sum)

        return total_points - min_sum

