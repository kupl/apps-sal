prime, idx = [2,3], [0,1,2,3]
def ensure(n):
    n0 = len(idx)
    if n <= n0: return
    prime.extend([ x for i,x in enumerate(idx[prime[-1] + 1:], prime[-1] + 1)
                 if i == x ])
    idx.extend(range(n0, n))
    for x in prime:
        for j in range(max(x, (n0 - 1) // x + 1) * x, n, x): idx[j] = x
    for i,x in enumerate(idx[n0:], n0):
        if n <= i * i: break
        if i != x: continue
        prime.append(x)
        for j in range(x * x, n, x): idx[j] = x
class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        ensure(max(A) + 1)
        best, src, dst, visited = 0, {}, {}, set()
        for x in A:
            x0, ps = x, set()
            while x != 1:
                p = idx[x]
                if p not in ps:
                    ps.add(p)
                    if p in dst: dst[p].add(x0)
                    else: dst[p] = {x0}
                x //= p
            if idx[x0] == x0: best = 1
            else: src[x0] = ps
        for p in dst:
            if p in visited: continue
            work, grp, xs = {p}, set(), set()
            while work:
                grp |= work
                old, work = work, set()
                for p in old:
                    xs |= dst[p]
                    for x in dst[p] - {p}: work |= src[x] - grp
            visited |= grp
            best = max(len(xs), best)
        return best
