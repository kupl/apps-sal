class Solution:

    def maxDistance(self, positions: List[int], m: int) -> int:
        positions.sort()

        def check(value) -> bool:
            last = positions[0]
            count = 1
            for pos in positions:
                if pos - last > value:
                    count += 1
                    last = pos
                    if count >= m:
                        return False
            return True
        (left, right) = (1, max(positions))
        while left < right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left
