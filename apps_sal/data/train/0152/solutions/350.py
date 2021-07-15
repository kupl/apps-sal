class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        mn = sys.maxsize
        mx = position[-1] - position[0]
        
        for i in range(1, len(position)):
            mn = min(mn, position[i] - position[i-1])
            
        def isPoss(diff):
            count = 1
            start = 0
            cd = 0
            f = sys.maxsize
            for i in range(1, len(position)):
                if cd + position[i] - position[i-1] < diff:
                    cd += position[i] - position[i-1]
                else:
                    count += 1
                    f = min(f, position[i] - position[start])
                    start = i
                    cd = 0
                    if count == m:
                        break
                    
            if count == m:
                return f
            return -1
        
        ans = -1
        while mn <= mx:
            mid = (mn + mx)//2
            v = isPoss(mid)
            if v != -1:
                ans = v
                mn = mid + 1
            else:
                mx = mid - 1
        return ans
        
            
            
        

