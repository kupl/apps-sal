class Solution:
    def racecar(self, target: int) -> int:

        q = [(0, 1)]
        vis = set([(0, 1)])
        ans = 0
        while q:
            new_q = []
            for p, s in q:
                if p == target:
                    return ans
                p1, s1 = p + s, 2 * s
                p2, s2 = p, -1 if s > 0 else 1
                # if (p1,s1) not in vis:
                #     vis.add((p1,s1))
                new_q.append((p1, s1))
                if (p2, s2) not in vis:
                    vis.add((p2, s2))
                    new_q.append((p2, s2))
            q = new_q
            ans += 1
        return -1
