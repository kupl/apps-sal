class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        left = 1
        right = position[-1] - position[0]
        
        def countBalls(dist):
            curr, balls = position[0], 1;
            for i in position:
                if (i-curr >= dist):
                    balls += 1
                    curr = i
            return balls
        
        while (left <= right):
            mid = (left + right) // 2
            if (countBalls(mid) >= m):
                left = mid + 1
            else:    
                right = mid - 1
        
        return right
            
            
                
        

