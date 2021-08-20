def count(position, m, n, d):
    (ans, curr) = (1, position[0])
    for i in range(1, n):
        if position[i] - curr >= d:
            ans += 1
            curr = position[i]
            if ans == m:
                return True
    return False


class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)
        (l, r) = (1, 10 ** 9 + 7)
        res = -1
        while l < r:
            mid = (l + r) // 2
            if count(position, m, n, mid):
                res = max(res, mid)
                l = mid + 1
            else:
                r = mid
        return res
