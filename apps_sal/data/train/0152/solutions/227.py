class Solution:

    def distribute(self, position, m, dist):
        prev = position[0]
        m -= 1
        for i in range(1, len(position)):
            if position[i] - prev >= dist:
                prev = position[i]
                m -= 1
            if m == 0:
                return True
        return False

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        (low, high) = (0, position[-1] - position[0])
        res = 0
        while low <= high:
            mid = (high - low) // 2 + low
            if self.distribute(position, m, mid):
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        return res
