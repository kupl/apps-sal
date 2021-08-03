class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        points = cardPoints[-k:] + cardPoints[:k]
        curr = 0
        max_ = 0
        for ind, score in enumerate(points):
            if ind >= k:
                curr -= points[ind - k]
            curr += score
            max_ = max(max_, curr)
        return max_
