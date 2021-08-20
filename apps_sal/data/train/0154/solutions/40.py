class Solution:

    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        (ph, pw) = (0, 0)
        (msh, msw) = (0, 0)
        for ch in horizontalCuts:
            if ch - ph > msh:
                msh = ch - ph
            ph = ch
        if h - ph > msh:
            msh = h - ph
        for cw in verticalCuts:
            if cw - pw > msw:
                msw = cw - pw
            pw = cw
        if w - pw > msw:
            msw = w - pw
        return msh * msw % (10 ** 9 + 7)
