class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if not cardPoints or len(cardPoints) == 0:
            return 0
        window = len(cardPoints) - k
        res = float('inf')
        s = 0
        for i in range(window):
            s += cardPoints[i]
        res = min(s, res)
        for i in range(window, len(cardPoints)):
            print(cardPoints[i],s,i)
            s -= cardPoints[i-window]
            s += cardPoints[i]
            res = min(s, res)
        return sum(cardPoints) - res
