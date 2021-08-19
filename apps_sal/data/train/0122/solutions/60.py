def max_score_using_subsequence(card_points, k):
    l = len(card_points) - k
    if l == 0:
        return sum(card_points)

    sum_subsequence = 0
    for i in range(l):
        sum_subsequence += card_points[i]

    lowest = sum_subsequence
    for i in range(len(card_points) - l):
        sum_subsequence = sum_subsequence - card_points[i] + card_points[i + l]
        if sum_subsequence < lowest:
            lowest = sum_subsequence

    return sum(card_points) - lowest


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # return max_score_recursive(cardPoints, k, 0, len(cardPoints)-1, {})
        return max_score_using_subsequence(cardPoints, k)
