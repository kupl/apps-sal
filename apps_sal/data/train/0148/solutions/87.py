class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        make=[0]*(10**5)
        num=[(difficulty[i],profit[i])for i in range(len(profit))]
        num.sort(key=lambda x:x[0])
        x=0
        while x<len(num):
            if x+1<len(num):
                if num[x][1]>num[x+1][1]:
                    num.pop(x+1)
                else:x+=1
            else:break
        for i in range(len(num)):
            make[num[i][0]]=num[i][1]
        pre=-1
        for i in range(len(make)):
            if make[i]!=0:
                pre=make[i]
            elif pre!=-1:
                make[i]=pre
        ans=0
        for w in worker:
            ans+=make[w]
        return ans    

