def check(x, pos, m):
    c = 0
    prev = -1000000000000000
    for i in range(len(pos)):
        if abs(pos[i] - prev) >= x:
            c += 1
            prev = pos[i]
    return c >= m


class Solution:

    def maxDistance(self, pos: List[int], m: int) -> int:
        pos.sort()
        n = len(pos)
        l = 1
        r = pos[-1]
        while l <= r:
            mid = l + (r - l) // 2
            if check(mid, pos, m):
                l = mid + 1
            else:
                r = mid - 1
        if check(l, pos, m):
            return l
        else:
            return r
