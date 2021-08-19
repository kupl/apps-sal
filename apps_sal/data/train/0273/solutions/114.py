class Solution:

    def racecar(self, t: int) -> int:
        q = [(0, 1, 0)]
        seen = {}
        while q:
            (c, s, step) = q.pop(0)
            if (c, s) in seen:
                continue
            else:
                seen[c, s] = step
            if c == t:
                return step
            step += 1
            c1 = c + s
            s1 = s * 2
            if abs(c + s - t) < t and (c1, s1) not in seen:
                q.append((c1, s1, step))
            s2 = -1 if s > 0 else 1
            if abs(c - t) < t and (c, s2) not in seen:
                q.append((c, s2, step))
        return -1
