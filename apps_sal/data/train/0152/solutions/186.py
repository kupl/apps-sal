class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        left = 1
        right = (position[-1] - position[0]) // (m - 1)

        def placeable(gap):
            count = 0
            x = -gap
            for n in position:
                if n - x >= gap:
                    count += 1
                    x = n
                    if count == m:
                        return True
            return False
        while left < right:
            mid = (left + right + 1) // 2
            if placeable(mid):
                left = mid
            else:
                right = mid - 1
        return left
