class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:

        Aindex = [(a, i) for i, a in enumerate(A)]
        Aindex.sort(key=lambda x: (x[0], x[1]))
        mn = len(A)
        ans = 0
        for a, i in Aindex:
            print((i, ans, i - mn, mn))
            ans = max(ans, i - mn)
            mn = min(mn, i)
        return ans
