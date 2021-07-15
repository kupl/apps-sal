class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        
        
        def check(min_force):
            count = 1
            k = position[0]
            for n in position:
                if n-k >= min_force:
                    count += 1
                    k = n
                    if count >= m:
                        return True
            return False
        
        
        i, j = 1, position[-1]-position[0]
        while i <= j:
            mid = (i+j)//2
            c1 = check(mid)
            c2 = check(mid+1)
            if c1 and not c2:
                return mid
            if not c1:
                j = mid-1
            else:
                i = mid+1
