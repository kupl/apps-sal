class Solution:
    def maxDistance(self, positions: List[int], m: int) -> int:
        positions.sort()
        def valid(mid):
            count = 0
            last = -math.inf
            for pos in positions:
                if pos >= last + mid:
                    count += 1
                    last = pos
            return count >= m
            
        left, right = 0, positions[-1]
        while left <= right:
            mid = (left + right) // 2
            if valid(mid):
                left = mid + 1
            else:
                right = mid - 1
        return right
