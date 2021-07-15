class Solution:
    def numWays(self, s: str) -> int:
        tot_ones=s.count('1')
        if tot_ones%3 !=0:
            return 0
        
        c=0
        ln=len(s)
        if tot_ones==0:
            return ((ln-2)*(ln-1)//2)%(10**9+7)
        fe=ss=se=ts=None
        for i,d in enumerate(s):
            if d=='1':
                c+=1
            
            if c==tot_ones//3 and fe is None:
                fe=i
            if c==tot_ones//3+1 and ss is None:
                ss=i
            if c==2*tot_ones//3 and se is None:
                se=i
            if c==2*tot_ones//3+1 and ts is None:
                ts=i
        
        return ((ss-fe)*(ts-se))%(10**9+7)
