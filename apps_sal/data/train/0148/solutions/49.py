class Solution:

    def maxProfitAssignment(self, d: List[int], p: List[int], work: List[int]) -> int:
        (N, maxd) = (len(p), max(d))
        cmb = [(d[i], p[i]) for i in range(N)]
        cmb.sort()
        dd = [0] * (maxd + 1)
        val = j = 0
        for i in range(maxd + 1):
            while j < N and i >= cmb[j][0]:
                val = max(val, cmb[j][1])
                j += 1
            dd[i] = val
        ans = 0
        for w in work:
            if w > maxd:
                ans += dd[maxd]
            else:
                ans += dd[w]
        return ans
