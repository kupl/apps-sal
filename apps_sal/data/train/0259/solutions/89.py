import math
def divisor(l, n):
    ans = 0
    
    for i in l:
        ans += math.ceil(i/n)
    return ans


class Solution:
    def smallestDivisor(self, l: List[int], t: int) -> int:
        if sum(l)<=t:
            return 1
        s = sum(l)
        ans = 0
        x = 0
        i = 1
        j = 1
        while(x<t):
            j = i
            x = divisor(l, i)
            if x<t:
                i *= 2 
            else:
                break
        mid = 0
        j = max(l)
        p = -1
        # print(i, j)
        
        while(i<j):
            
            mid = (i+j)//2
            x = divisor(l, mid)
            # print('mid',x, mid)                
            if x<t:
                j = mid
            elif x == t:
                break
            else:
                i = mid+1
            if i == j:
                mid = j
                break
        
        while(1):
            # print(mid)
            x = divisor(l, mid-1)
            if x <= t:
                mid -= 1
            else:
                break
                
        return mid
                
                        
        
        

