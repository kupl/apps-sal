class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        posSorted = position
        low = 1
        high = posSorted[-1]
        mid = (low+high)//2

        while low < high:
            if self.validForce(posSorted, m, mid):
               low = mid
            else:
                high = mid-1

            mid = high-(high-low)//2
        
        return low 

    def validForce(self, positions, m, mid):
        used = 0
        lastpos = 0
        for i, pos in enumerate(positions):
            if i == 0:
                used += 1
                continue
            if (pos - positions[lastpos]) >= mid:
                lastpos = i  
                used += 1
        if used >= m:
            return True

        return False
