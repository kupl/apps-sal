class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        dp = {}
        for i, d in enumerate(difficulty):
            dp[d] = max(profit[i], dp.get(d, 0))
        dp = sorted([(d, p) for d, p in dp.items()])

        d2p = []
        pre = 0
        for d, p in dp:
            pre = max(pre, p)
            d2p.append((d, pre))

        def getjob(work, pv, pw, pi):
            l, r = 0, len(d2p) - 1
            if d2p[l][0] > work:
                return 0, 0
            if d2p[r][0] <= work:
                return d2p[r][1], r
            l = pi

            while l <= r:
                i = (l + r) // 2
                if d2p[i][0] == work:
                    return max(d2p[i][1], pv), i
                if d2p[i][0] > work:
                    r = i - 1
                else:
                    l = i + 1
            if i == r:
                return max(d2p[i][1], pv), i
            return max(d2p[i - 1][1], pv), i - 1

        rs = 0
        pv = 0
        pw = 0
        pi = 0
        for w in sorted(worker):
            pv, pi = getjob(w, pv, pw, pi)
            pw = w
            rs += pv
        return rs
