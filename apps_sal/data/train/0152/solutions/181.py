class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position) 
        
        def checkForce(force, positions, m):
            prev = positions[0]
            i = 1
            while m > 0 and i < len(positions):
                while positions[i] - force < prev:
                    i += 1
                    if i >= len(positions): return False
                m -= 1
                prev = positions[i]
                i += 1
            return m <= 0
        
        # print(checkForce(2, position, m - 1))
        l, r = 0, position[-1] - position[0]
        while l < r:
            mid = r - (r - l) // 2
            # force is acceptable, let's see if we can achieve a higher force 
            if checkForce(mid, position, m-1):
                l = mid
            else:
                r = mid - 1
        return l 

