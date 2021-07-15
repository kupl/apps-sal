class Solution:
    def possible(self, position, dist, m):
        prev = float('-inf')
        cnt = 0
        for x in position:
            if x < prev + dist:
                continue
            cnt += 1
            prev = x
        return cnt >= m
        
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        
        low, high = 0, max(position)
        while low + 1 < high:
            mid = (low + high) // 2
            if self.possible(position, mid, m):
                low = mid
            else:
                high = mid
        
        if self.possible(position, high, m):
            return high
        
        return low
                

