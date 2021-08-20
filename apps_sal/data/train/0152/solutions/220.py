class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        maxrange = position[-1] - position[0]
        (l, r) = (1, maxrange)
        while l <= r:
            mid = l + (r - l) // 2
            cnt = self.count(position, mid)
            if cnt >= m:
                l = mid + 1
            else:
                r = mid - 1
        return r

    def count(self, poss: list, dist: int) -> int:
        res = 1
        last = poss[0]
        for i in range(1, len(poss)):
            if poss[i] - last >= dist:
                res += 1
                last = poss[i]
        return res
