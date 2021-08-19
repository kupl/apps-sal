class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        left = 1
        right = max(position)
        position.sort()
        while left < right:
            mid = left + (right - left) // 2
            legal = self.evaluate(position, m, mid)
            if legal:
                right = mid
            else:
                left = mid + 1
        return left - 1

    def evaluate(self, position, m, force):
        balls_placed = 0
        prev_val = None
        for val in position:
            if not prev_val:
                prev_val = val
                balls_placed += 1
            elif val - prev_val >= force:
                balls_placed += 1
                prev_val = val
        if balls_placed > m - 1:
            return False
        return True
