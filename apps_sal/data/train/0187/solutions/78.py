class Solution:

    def minOperationsMaxProfit(self, cc: List[int], bc: int, rc: int) -> int:
        if 4 * bc < rc:
            return -1
        (pf, rt) = (0, 0)
        pfc = 0
        (i, ac) = (0, 0)
        n = len(cc)
        while i < n or ac > 0:
            if i < n:
                ac += cc[i]
            vc = 4 if ac >= 4 else ac
            p1 = vc * bc - rc
            pfc = p1 + pfc
            if pfc > pf:
                pf = pfc
                rt = i + 1
            ac -= vc
            i += 1
        return rt
