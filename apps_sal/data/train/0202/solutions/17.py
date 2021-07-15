class Solution:
    def longestMountain(self, A: List[int]) -> int:
        
        ans = 0
        temp = 0
        trend = False
        
        if len(A)<3: return 0
        good = False
        
        for i in range(1,len(A)):
            
            diff = A[i]-A[i-1]
            if diff>0:
                if not trend:
                    good = True
                    trend = True
                    temp = 2
                else:
                    temp=max(temp+1,2)
            elif diff<0:
                if trend:
                    trend = False
                    temp = max(temp+1,2)
                    ans = max(ans,temp)
                else:
                    temp=max(temp+1,2)
                    if good: ans = max(ans,temp)
            else:
                temp = 0
                trend = False
                good = False
            print(A[i], temp,trend, ans)
        
        # ans = max(ans,temp)
            
        return ans
