class Solution:

    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        q1 = [tuple(source)]
        q2 = [tuple(target)]
        vis1 = set([tuple(source)])
        vis2 = set([tuple(target)])
        blocked = set([tuple(b) for b in blocked])
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def valid(r, c):
            if r >= 0 and r < 1000000 and (c >= 0) and (c < 1000000):
                return True
            return False
        while q1 and q2:
            if len(q1) > len(blocked) and len(q2) > len(blocked):
                return True
            temp = []
            for (r, c) in q1:
                if (r, c) in vis2:
                    return True
                for d in dirs:
                    nr = r + d[0]
                    nc = c + d[1]
                    if valid(nr, nc):
                        if (nr, nc) not in vis1 and (nr, nc) not in blocked:
                            temp.append((nr, nc))
                            vis1.add((nr, nc))
            q1 = temp
            temp = []
            for (r, c) in q2:
                if (r, c) in vis1:
                    return True
                for d in dirs:
                    nr = r + d[0]
                    nc = c + d[1]
                    if valid(nr, nc):
                        if (nr, nc) not in vis2 and (nr, nc) not in blocked:
                            temp.append((nr, nc))
                            vis2.add((nr, nc))
            q2 = temp
        return False
