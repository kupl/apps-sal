class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)
        # distances = [i for i in range(10**9)]
        # distances.sort()
        
        
        hi = 10**9-1
        li = 0
        while li <= hi:
            # print(\"li \",li,\"hi \",hi)
            if li == hi:
                return li
            mid = (hi+li)//2
            if hi == li+1:
                mid += 1
                
            d = mid
            i = 0
            j = 0
            count = 1
            flag = True

            while count < m:
                while position[j]<position[i] + d:
                    j += 1
                    if j == n and count < m:
                        flag = False
                        break
                if j == n and count <m:
                    flag = False
                    break
                i = j
                count += 1
                
            if hi == li+1:
                if flag:    
                    return hi
                else:
                    return li
            
    
            if flag:
                li = mid
            else:
                hi = mid-1
            
            
                    
    

