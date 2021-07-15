class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        cur, ans = 0, 0
        for a in  A:
            ans = max(ans, cur + a)
            cur = max(cur, a) -1
        return ans

