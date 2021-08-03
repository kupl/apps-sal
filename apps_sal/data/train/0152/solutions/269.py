class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)
        high = position[-1] - position[0]
        low = 1
        while high != low:
            mid = (high + low + 1) // 2
            balls = 1
            start = position[0]
            for i in range(1, n):
                if position[i] - start >= mid:
                    balls += 1
                    start = position[i]
            if balls >= m:
                low = mid
            else:
                high = mid - 1
        return low
