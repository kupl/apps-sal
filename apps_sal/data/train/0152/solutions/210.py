class Solution:
    # min-max, dp?
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        
        def feasible(dist):
            placed, pos = 0, 0
            prev = float('-inf')
            while pos < len(position):
                if position[pos] - prev >= dist:  # can place one more
                    placed += 1
                    prev = position[pos]
                pos += 1
                if placed == m:
                    return True
            return False
                
        
        left, right = 1, position[-1]
        while left < right:
            dist = (left + right) // 2
            if feasible(dist):
                left = dist + 1
            else:
                right = dist
                
        return left - 1
        
                
                
                
                
        

