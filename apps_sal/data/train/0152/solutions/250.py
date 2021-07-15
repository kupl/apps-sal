class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        start, end = 0, position[-1]
    
        while start + 1 < end:
            mid = (start + end) // 2
            if self.isValid(position, mid) < m:
                end = mid
            else:
                start = mid
                
        if self.isValid(position, end) < m:
            return start
        else:
            return end
        
        
    def isValid(self, position, dist):
        cnt = 1
        i = 1
        current = position[0] + dist
        while i < len(position):
            if position[i] >= current:
                cnt += 1
                current = position[i] + dist
            i += 1
        return cnt
        
            


