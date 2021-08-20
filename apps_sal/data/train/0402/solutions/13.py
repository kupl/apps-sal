class Solution:

    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        blocked = set([tuple(b) for b in blocked])
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def valid(r, c):
            if r >= 0 and r < 1000000 and (c >= 0) and (c < 1000000):
                return True
            return False

        def bfs(source, target):
            q = [tuple(source)]
            vis = set([tuple(source)])
            while q:
                if len(q) > len(blocked):
                    return True
                temp = []
                for (r, c) in q:
                    if (r, c) == tuple(target):
                        return True
                    for d in dirs:
                        nr = r + d[0]
                        nc = c + d[1]
                        if valid(nr, nc):
                            if (nr, nc) not in vis and (nr, nc) not in blocked:
                                temp.append((nr, nc))
                                vis.add((nr, nc))
                q = temp
            return False
        return bfs(source, target) and bfs(target, source)
