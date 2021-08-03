from collections import defaultdict


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:

        br = []
        start_r = []
        for i, r in enumerate(routes):
            br.append(set(r))
            if S in r:
                start_r.append(i)

        if S == T:
            return 0

        g = defaultdict(set)
        for i in range(len(br)):
            for j in range(i + 1, len(br)):
                if br[i].intersection(br[j]):
                    g[i].add(j)
                    g[j].add(i)

        def bfs(r):
            it = 1
            q = [r]
            vs = set()

            while q:
                tmp = []
                for ele in q:
                    if ele in vs:
                        continue
                    vs.add(ele)
                    if T in br[ele]:
                        return it
                    for n in g[ele]:
                        tmp.append(n)
                q = tmp
                it += 1

            return math.inf

        res = math.inf
        for r in start_r:
            res = min(res, bfs(r))

        return res if res != math.inf else -1
