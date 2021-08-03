class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        position.sort()
        min_p, max_p = position[0], position[-1]

        def enough(x):
            prev, cnt = min_p, 1
            for i, p in enumerate(position):
                if p - prev >= x:
                    prev = p
                    cnt += 1

                    if cnt >= m:
                        return True
            return False

        l, r = 1, max_p - min_p
        while l < r:
            mid = (l + r + 1) // 2
            if enough(mid):
                l = mid
            else:
                r = mid - 1
        return l
