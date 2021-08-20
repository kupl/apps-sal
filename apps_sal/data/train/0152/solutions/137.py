class Solution:

    def maxDistance(self, pos: List[int], m: int) -> int:
        pos.sort()

        def check(force, m):
            last = pos[0]
            m -= 1
            for i in range(1, len(pos)):
                if pos[i] - last >= force:
                    last = pos[i]
                    m -= 1
                if not m:
                    return True
            return False
        (left, right) = (2, 10 ** 9)
        while left <= right:
            mid = left + (right - left) // 2
            if check(mid, m):
                left = mid + 1
            else:
                right = mid - 1
        return right
