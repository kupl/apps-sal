class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # position = sorted(position)
        # def enough(distance):
        #     cur = position[0]
        #     c = 1
        #     for i in range(len(position)):
        #         if position[i] >= cur + distance:
        #             cur = position[i]
        #             c += 1
        #     return c>=m
        # cur_max = position[-1]-position[0] + 1
        # cur_min = 1
        # while abs(cur_min-cur_max)>1:
        #     mid = cur_min + (cur_max-cur_min)//2
        #     if enough(mid):
        #         cur_min = mid
        #     else:
        #         cur_max = mid
        # return cur_min
    
        position = sorted(position)
        n = len(position)
        if n == 2:
            return position[-1]-position[0]
        
        cur_min = 1
        cur_max = position[-1]-position[0]+1
        
        def enough(distance):
            ini = position[0]
            c = 1
            for i in range(1, n):
                if position[i]-ini >= distance:
                    ini = position[i]
                    c += 1
                
            return c>=m
            
        while(abs(cur_max-cur_min)>1):
            mid = (cur_max+cur_min)//2
            if enough(mid):
                cur_min = mid
            else:
                cur_max = mid
        
        return cur_min

