class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        left, right = 1, (position[-1] - position[0]) // (m - 1) + 2
        while left < right:
            mid = left + (right - left) // 2 + 1

            if self.can_use_as_min(position, mid, m):
                left = mid
            else:
                right = mid - 1

        return left

    def can_use_as_min(self, position, min_distance, m):
        m -= 1
        i = 1
        last_position = position[0]

        while m > 0:
            while position[i] - last_position < min_distance:
                i += 1

                if i >= len(position):
                    return False

            last_position = position[i]
            m -= 1

        return True
