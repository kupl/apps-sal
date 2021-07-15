class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        ans = []
        for nn in range(lo,hi+1):
            ans.append([nn,self.powerVal(nn)])
        ans = sorted(ans,key=lambda x:x[1])
        return ans[k-1][0]
        
    def powerVal(self, num):
        count = 0 
        while num>1:
            if num%2==0:
                num = num/2
            else:
                num = 3*num+1
            count +=1
        return count
