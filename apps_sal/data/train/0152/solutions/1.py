class Solution:
    def maxDistance(self, p: List[int], m: int) -> int:

        def isvalid(f: int):
            buckets, pos = 1, p[0]
            for x in p:
                if f <= x - pos:
                    buckets += 1
                    if buckets == m:
                        return True
                    pos = x
            return False

        p.sort()
        lb, ub = 1, (p[-1] - p[0]) // (m - 1) + 1

        while 1 < ub - lb:

            f = (lb + ub) // 2

            if isvalid(f):
                lb = f
            else:
                ub = f

        return lb
