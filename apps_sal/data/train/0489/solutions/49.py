class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        N = 50001
        sms = [None] * N
        lgs = [None] * N

        for i, x in enumerate(A):
            if sms[x] is None:
                sms[x] = i
            lgs[x] = i

        m = 0
        ss = float('inf')
        for x in range(N):
            if lgs[x] is None:
                continue
            ss = min(ss, sms[x])
            m = max(m, lgs[x] - ss)

        return m
