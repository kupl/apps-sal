class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        res = {}
        if(lo==1 and hi==1 and k==1):
            return 1
        
        def count_steps(x):
            cnt = 0
            if(x==1):
                return cnt;
            while(x>1):
                if x%2 == 0:
                    x = x//2
                else:
                    x = x*3 + 1
                cnt+=1
            return cnt
        
        for i in range(lo,hi+1):
            res[i] = count_steps(i)
        return sorted(list(res.items()),key = lambda x:x[1])[k-1][0]


