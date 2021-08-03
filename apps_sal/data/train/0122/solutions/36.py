class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        right_index = len(cardPoints) - k
        curr_max = sum(cardPoints[right_index:])
        curr_sum = curr_max
        for left_index in range(0, k):
            curr_sum -= cardPoints[right_index]
            right_index += 1
            curr_sum += cardPoints[left_index]
            if curr_sum > curr_max:
                curr_max = curr_sum
        return curr_max
