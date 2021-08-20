class Solution:

    def isPossible(self, position, m, force):
        lastKept = position[0]
        m -= 1
        for i in range(1, len(position)):
            currentPosition = position[i]
            if currentPosition - lastKept >= force:
                lastKept = currentPosition
                m -= 1
        return m <= 0

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        (left, right) = (1, 10 ** 9 + 1)
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if self.isPossible(position, m, mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        return result
