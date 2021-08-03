class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # Time: O(k)
        # Space: O(1)
        ans = win = 0
        for i in range(-k, k):
            win += cardPoints[i]
            if i >= 0:
                win -= cardPoints[i - k]
            #print(i, i-k, ans, win, cardPoints[i] )
            ans = max(win, ans)
        return ans
