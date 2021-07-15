class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        res = -1
        if m == 2:
            return position[-1]-position[0]
        
        def count(spacing):
            count = 1
            prev_pos = position[0]
            for pos in position:
                if pos-prev_pos>=spacing:
                    count+=1
                    prev_pos = pos
            return count
        
        
        left,right = 1,math.ceil(position[-1]/(m-1))
        while left<=right:
            mid = (left+right)//2
            if count(mid)>=m:
                res = mid
                left = mid+1
            else:
                right = mid-1
        
        return res
