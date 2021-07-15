class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        n = len(arr)
        if sum(arr) <= target:
            return max(arr)
        
        left, right = 0, max(arr)
        
        while(left <= right):
            
            #print(left, right)
            if left == right:
                return left
            
            if left == right -1:
                sleft, sright = 0, 0
                
                for a in arr:
                    if a < left:
                        sleft += a
                    else:
                        sleft += left
                    
                    if a < right:
                        sright += a
                    else:
                        sright += right
                
                if abs(sleft - target) <= abs(sright - target):
                    return left
                else:
                    return right
                
            mid = (left + right) // 2
            midarr = []
            
            for a in arr:
                if a < mid:
                    midarr.append(a)
                else:
                    midarr.append(mid)
            
            midsum = sum(midarr)
            if midsum < target:
                    
                left = mid
            else:
                right = mid
        

