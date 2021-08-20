class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()
        left = 1
        right = max(position)
        while right - left > 1:
            mid = (left + right) // 2
            if self.ok(position, m, mid):
                left = mid
            else:
                right = mid
        if self.ok(position, m, right):
            return right
        elif self.ok(position, m, left):
            return left

    def ok(self, position, m, force):
        n = len(position)
        stack = [position[0]]
        i = 0
        while i < n:
            if position[i] - stack[-1] >= force:
                stack.append(position[i])
            i += 1
        return len(stack) >= m
