from collections import defaultdict
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        '''
        x*k = num1 + num2 = a*k+remain1 + b*k+remain2
                        = (a+b)*k + remain1+remain2
                        remain1+remain2 = k,-k or 0
        
        
        [1,2,3,4,5,10,6,7,8,9]
        
        [1,2,3,4,0,0,1,2,3,4]
        '''
        
        d = defaultdict(int)
        for num in arr:
            sgn = 1 if num >= 0 else -1
            num = sgn*(abs(num)%k)
            if num==0:
                if d[0]:
                    d[0]-=1
                    if d[0]==0: del d[0]
                else:
                    d[0]+=1
            else:
                if -num in d and d[-num]:
                    d[-num]-=1
                    if d[-num]==0: del d[-num]
                elif -k-num in d and d[-k-num]:
                    d[-k-num]-=1
                    if d[-k-num]==0: del d[-k-num]
                elif k-num in d and d[k-num]:
                    d[k-num]-=1
                    if d[k-num]==0: del d[k-num]
                else:
                    d[num]+=1
        return len(d)==0
