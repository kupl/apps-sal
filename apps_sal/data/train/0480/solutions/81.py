class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        c_ori=[0]*min(steps+2,(2+arrLen))
        c_ori[1]=1
        c_new=[0]*min(steps+2,(2+arrLen))
        
        for i in range(0,steps):
            for j in range(1,len(c_ori)-1):
                c_new[j]=c_ori[j]+c_ori[j-1]+c_ori[j+1]
            #print(c_new)
            c_ori=c_new.copy()
        return c_ori[1]%1000000007

