class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def valid(force):
            nonlocal position, m

            start = count = 0
            for index, value in enumerate(position):
                if value - force >= position[start]:
                    count += 1
                    start = index

            return count >= m - 1

        lo, hi = 1, position[-1] - position[0]
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2

            if valid(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo
