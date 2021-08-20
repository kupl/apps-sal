class node:

    def __init__(self, val):
        self.val = val
        self.next = []


class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        p = [2]
        for i in range(3, int(max(A) ** 0.5) + 1, 2):
            for y in p:
                if i % y == 0:
                    break
            else:
                p.append(i)
        f = collections.defaultdict(list)
        for a in A:
            x = a
            for pp in p:
                if pp ** 2 > x:
                    break
                if x % pp == 0:
                    f[a].append(pp)
                    while x % pp == 0:
                        x = x // pp
            if x > 1:
                f[a].append(x)
                p.append(x)
        p = list(set(p))
        n = len(p)
        p2i = {pp: i for (i, pp) in enumerate(p)}
        par = [i for i in range(n)]

        def find(i):
            if i != par[i]:
                par[i] = find(par[i])
            return par[i]

        def union(i, j):
            (pi, pj) = (find(i), find(j))
            if pi != pj:
                par[pi] = pj
        for a in A:
            if f[a]:
                p0 = f[a][0]
                for pp in f[a][1:]:
                    union(p2i[p0], p2i[pp])
        c = collections.Counter((find(p2i[f[a][0]]) for a in A if f[a]))
        return max(c.values())
