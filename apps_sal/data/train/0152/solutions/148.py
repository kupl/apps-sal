class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        N = len(position)
        
        left, right = 0, position[-1] - position[0]
        
        while left + 1 < right:
            mid = int((right - left) / 2 + left)
            
            if self.count(mid, position) >= m:
                left = mid
            else:
                right = mid
        
        if self.count(right, position) == m:
            return right
        return left
    
    def count(self, n: int, position: List[int]) -> int:
        ans, curr = 1, position[0]
        
        for i in range(1, len(position)):
            if position[i] - curr >= n:
                curr = position[i] 
                ans += 1
                
        return ans
