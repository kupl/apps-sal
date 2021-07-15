class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def realizable(value):
            last = position[0]
            placed = 1
            for k in range(1, len(position)):
                if position[k] - last >= value:
                    placed += 1
                    last = position[k]
            return placed >= m
        
        min_dist, max_dist = position[1] - position[0], position[-1] - position[0]
        for k in range(1,len(position)):
            min_dist = min(min_dist, position[k]-position[k-1])
        
        left, right = min_dist, max_dist + 1
        print(left, right)
        while left < right:
            mid = left + (right - left) // 2
            if not realizable(mid):
                right = mid
            else:
                left = mid + 1
        return left - 1
