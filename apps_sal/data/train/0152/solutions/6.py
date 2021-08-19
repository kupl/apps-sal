class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        return self.binaryS(0, position[-1], position, m)

    def binaryS(self, left, right, position, m):
        while left < right:
            mid = (left + right) // 2
            val = self.check(position, mid + 1, m)
            if val:
                left = mid + 1
            else:
                right = mid
        return right

    def check(self, position, interval, m) -> bool:
        total = 1
        start = position[0]
        for i in range(1, len(position)):
            if position[i] - start >= interval:
                total += 1
                start = position[i]
        return total >= m
