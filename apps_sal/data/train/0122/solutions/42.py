class Solution:

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if len(cardPoints) < k:
            return -1
        remain = len(cardPoints) - k
        suum = sum(cardPoints[:remain])
        min_suum = suum
        for i in range(remain, len(cardPoints)):
            suum = suum - cardPoints[i - remain] + cardPoints[i]
            min_suum = min(min_suum, suum)
        return sum(cardPoints) - min_suum
