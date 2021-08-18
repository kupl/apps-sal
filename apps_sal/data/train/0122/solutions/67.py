class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        ans = win = 0
        for i in range(-k, k):
            win += cardPoints[i]
            if i >= 0:
                win -= cardPoints[i - k]
            ans = max(win, ans)
        return ans
