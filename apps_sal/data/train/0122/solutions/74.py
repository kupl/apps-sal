class Solution:

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        right_index = len(cardPoints) - k
        curr_max = sum(cardPoints[right_index:])
        curr_sum = curr_max
        for (left_index, right_index) in zip(list(range(0, k)), list(range(len(cardPoints) - k, len(cardPoints)))):
            print((left_index, right_index))
            curr_sum -= cardPoints[right_index]
            curr_sum += cardPoints[left_index]
            curr_max = max(curr_max, curr_sum)
        return curr_max
