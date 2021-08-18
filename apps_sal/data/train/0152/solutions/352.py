class Solution:
    def maxDistance(self, position, m):
        position.sort()
        n = len(position)

        def canFit(gap):
            ct = 1
            i = 0
            j = 1
            while j < n:
                while j < n and position[j] - position[i] < gap:
                    j += 1
                if j < n:
                    ct += 1
                    i = j
                    j += 1

                if ct == m:
                    return True
            return False

        lo = 1
        hi = position[-1] - position[0]
        res = 0
        ct = 0
        while lo <= hi:
            mid = (lo + hi) >> 1
            ct += 1
            if canFit(mid):
                res = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return res
