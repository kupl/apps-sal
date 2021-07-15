class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)
        left,right = 0,position[-1]-position[0] // (m-1) # search space is sorted
        def count_balls(force):
            balls,prev = 1,position[0]
            for cur in position[1:]:
                if cur-prev >= force:
                    balls += 1
                    prev = cur
            return balls
        while left < right:
            # mid = left + (right-left)//2
            mid = right - (right-left) // 2
            # mid = (left+right+1)//2
            if count_balls(mid) >= m:
                left = mid
            else:
                right = mid - 1
        return left

            
            
            
            

