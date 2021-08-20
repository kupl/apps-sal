class Solution:

    def maxDistance(self, pos: List[int], m: int) -> int:
        pos.sort()

        def isfeasible(dist):
            cur = pos[0]
            n = 1
            for i in range(len(pos)):
                if pos[i] >= cur + dist:
                    cur = pos[i]
                    n += 1
            return n >= m
        ng = pos[-1] - pos[0] + 1
        ok = 1
        while abs(ok - ng) > 1:
            mid = ok + (ng - ok) // 2
            if isfeasible(mid):
                ok = mid
            else:
                ng = mid
        return ok
