class Solution:

    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        from fractions import Fraction
        workers = sorted(((Fraction(w, q), q, w) for (q, w) in zip(quality, wage)))
        ans = float('inf')
        pool = []
        sumq = 0
        for (ratio, q, w) in workers:
            heapq.heappush(pool, -q)
            sumq += q
            if len(pool) > K:
                sumq += heapq.heappop(pool)
            if len(pool) == K:
                ans = min(ans, ratio * sumq)
        return float(ans)
        n = len(wage)
        if K > n:
            return float(0)
        re = []
        re.append(float('inf'))
        self.util(quality, wage, 0, [], K, re)
        return re[0]

    def util(self, q, w, i, p, k, re):
        if len(p) == k:
            s = sum([t[1] for t in p])
            if s < re[0]:
                re[0] = s
        if i == len(w):
            return
        self.util(q, w, i + 1, [x[:] for x in p], k, re)
        if not p:
            p.append([q[i], w[i]])
            self.util(q, w, i + 1, [x[:] for x in p], k, re)
        else:
            price = p[0][1] * q[i] / p[0][0]
            if price > w[i]:
                p.append([q[i], price])
                self.util(q, w, i + 1, [x[:] for x in p], k, re)
            else:
                for idx in p:
                    idx[1] = w[i] * idx[0] / q[i]
                p.append([q[i], w[i]])
                self.util(q, w, i + 1, [x[:] for x in p], k, re)
