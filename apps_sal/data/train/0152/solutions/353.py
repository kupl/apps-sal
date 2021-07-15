class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        if len(position) < m: return 0
        
        position.sort()
        
        def can(force):
            cnt = 1
            pos = 0
            for i in range(1, len(position)):
                if position[i] - position[pos] >= force:
                    cnt += 1
                    pos = i
            return cnt >= m
        
        
        low, high = 0, position[-1] - position[0]
        while low < high:
            mid = (low + high + 1) // 2
            if can(mid):
                low = mid
            else:
                high = mid - 1
        return low
