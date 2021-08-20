class Solution:

    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        bl = {tuple(b) for b in blocked}
        (s0, s1) = source
        (t0, t1) = target
        s_vis = {(s0, s1)}
        t_vis = {(t0, t1)}
        s_q = [(s0, s1)]
        t_q = [(t0, t1)]
        while s_q and len(s_vis) < 20010:
            (n0, n1) = s_q.pop()
            if (n0, n1) == (t0, t1):
                return True
            if n0 < 10 ** 6 - 1 and (n0 + 1, n1) not in s_vis and ((n0 + 1, n1) not in bl):
                s_q.append((n0 + 1, n1))
                s_vis.add((n0 + 1, n1))
            if n0 > 0 and (n0 - 1, n1) not in s_vis and ((n0 - 1, n1) not in bl):
                s_q.append((n0 - 1, n1))
                s_vis.add((n0 - 1, n1))
            if n1 < 10 ** 6 - 1 and (n0, n1 + 1) not in s_vis and ((n0, n1 + 1) not in bl):
                s_q.append((n0, n1 + 1))
                s_vis.add((n0, n1 + 1))
            if n1 > 0 and (n0, n1 - 1) not in s_vis and ((n0, n1 - 1) not in bl):
                s_q.append((n0, n1 - 1))
                s_vis.add((n0, n1 - 1))
        while t_q and len(t_vis) < 20010:
            (n0, n1) = t_q.pop()
            if (n0, n1) == (s0, s1):
                return True
            if n0 < 10 ** 6 - 1 and (n0 + 1, n1) not in t_vis and ((n0 + 1, n1) not in bl):
                t_q.append((n0 + 1, n1))
                t_vis.add((n0 + 1, n1))
            if n0 > 0 and (n0 - 1, n1) not in t_vis and ((n0 - 1, n1) not in bl):
                t_q.append((n0 - 1, n1))
                t_vis.add((n0 - 1, n1))
            if n1 < 10 ** 6 - 1 and (n0, n1 + 1) not in t_vis and ((n0, n1 + 1) not in bl):
                t_q.append((n0, n1 + 1))
                t_vis.add((n0, n1 + 1))
            if n1 > 0 and (n0, n1 - 1) not in t_vis and ((n0, n1 - 1) not in bl):
                t_q.append((n0, n1 - 1))
                t_vis.add((n0, n1 - 1))
        return bool(t_q and s_q)
