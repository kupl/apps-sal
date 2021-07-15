class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        res = 0
        l, r = 1, (position[-1] - position[0]) // (m - 1) + 1
        
        while l < r:
            mid = (l + r) // 2
            prev = position[0]
            ball = 1
            for i in position[1:]:
                if i - prev >= mid:
                    ball += 1
                    if ball == m:
                        break
                    prev = i
                    
            if ball == m:
                l = mid + 1
                res = mid
            else:
                r = mid
        return res
        
                

