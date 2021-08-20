class Solution:

    def maxDistToClosest(self, seats: List[int]) -> int:
        (left, right) = (-1, 0)
        result = 0
        for right in range(len(seats)):
            if seats[right] == 0:
                continue
            if seats[right] == 1:
                if left == -1:
                    result = right
                else:
                    result = max((right - left) // 2, result)
                left = right
        if not seats[right]:
            result = max(result, right - left)
        return result
