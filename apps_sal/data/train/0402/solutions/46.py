from queue import PriorityQueue


class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:

       # Column and row of source and target (used for escape condition)
        sc, sr = source
        tc, tr = target
        R, C = 10**6, 10**6

        def dist(r1, c1, r2, c2):
            '''Calculates Manhattan distance from (r1,c1) to (r2,c2)'''
            return abs(r2 - r1) + abs(c2 - c1)

        # Two priority queues: one starting from target and one from source
        # Two visited sets: one for nodes visited by path from target and the other from source
        q = [[(0, *source[::-1])], [(0, *target[::-1])]]
        v = [set(), set()]
        b = set((tuple(b[::-1]) for b in blocked))

        if (tuple(source) in b) or (tuple(target) in b):
            return False

        # if source and target can reach 200 distance from their origin
        # it is safe to say 200 blocked spaces cannot contain them
        source_escape = False
        target_escape = False

        while q[0] and q[1]:

            index = 0 if len(q[0]) <= len(q[1]) else 1

            d, r, c = heapq.heappop(q[index])

            for i, j in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if (0 <= i < R) and (0 <= j < C) and ((i, j) not in b) and ((i, j) not in v[index]):

                    if (i, j) in v[1 - index]:
                        return True

                    v[index].add((i, j))
                    r_target, c_target = q[1 - index][0][1:]
                    heapq.heappush(q[index], (dist(i, j, r_target, c_target), i, j))

            if not source_escape and not index:
                source_escape = dist(r, c, sr, sc) > 200
            if not target_escape and index:
                target_escape = dist(r, c, tr, tc) > 200

            if source_escape and target_escape:
                return True

        return False
