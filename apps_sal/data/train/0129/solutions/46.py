class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        cur=res=0
        for i,a in enumerate(A):
            print(res, cur)
            res = max(res,  cur + a - i)
            cur = max(cur, a + i)
        return res
