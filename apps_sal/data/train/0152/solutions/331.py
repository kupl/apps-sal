class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        (l, r) = (0, 10 ** 9 + 2)
        while l < r:
            mid = (l + r) // 2
            prev = position[0]
            cnt = 1
            for p in position:
                if p >= prev + mid:
                    prev = p
                    cnt += 1
            if cnt < m:
                r = mid
            else:
                l = mid + 1
        return l - 1
