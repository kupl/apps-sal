class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        max_score = 0
        curr_score = 0
        init_hand = cardPoints[len(cardPoints) - k:]
        max_score = sum(init_hand)
        curr_score = max_score
        for i in range(k):
            curr_score -= init_hand[i]
            curr_score += cardPoints[i]
            if curr_score > max_score:
                max_score = curr_score
        return max_score
