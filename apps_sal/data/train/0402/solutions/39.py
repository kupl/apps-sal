class Solution:

    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:

        def bfs(s, t, b):
            (q, v) = ([s], {s})
            while len(q) > 0:
                (i, j) = q.pop(0)
                if (i, j) == t:
                    return True
                if i in (s[0] + 210, s[0] - 210) or j in (s[1] + 210, s[1] - 210):
                    return True
                for (d, e) in ((i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)):
                    if d >= 0 and d < 10 ** 6 and (e >= 0) and (e < 10 ** 6) and ((d, e) not in v) and ((d, e) not in b):
                        v.add((d, e))
                        q.append((d, e))
            return False
        b = set((tuple(i) for i in blocked))
        return bfs(tuple(source), tuple(target), b) and bfs(tuple(target), tuple(source), b)
