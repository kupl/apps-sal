class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def helper(distance):
            balls = m - 1
            previous = position[0]
            for i in position[1:]:
                if i - previous >= distance:
                    balls -= 1
                    if balls == 0:
                        return True
                    previous = i
            return False

        position.sort()
        min_distance = 1
        max_distance = (position[-1] - position[0]) // (m - 1)
        result = 1
        while min_distance <= max_distance:
            mid = (min_distance + max_distance) // 2
            if helper(mid):
                result = mid
                min_distance = mid + 1
            else:
                max_distance = mid - 1
        return result
