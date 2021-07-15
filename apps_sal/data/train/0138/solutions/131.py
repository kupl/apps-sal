class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        record=[]
        index=[-1]
        for i,j in enumerate(nums):
            if j>0:
                record.append(1)
            elif j<0:
                record.append(-1)
            else:
                record.append(0)
                index.append(i)
        # print(record,index)
        index.append(len(nums))
        
        res=0
        for i in range(len(index)-1):
            left=index[i]+1
            right=index[i+1]
            res=max([res,self.getMax(record[left:right])])
            #print(left,right,res)
        return res
        
    
    def getMax(self,arr):
        tot=1
        Cum=[1]
        for i in range(len(arr)):
            tot*=arr[i]
            Cum.append(tot)
            
        for k in range(len(arr),0,-1):
            for j in range(0,len(arr)-k+1):
                tmp=Cum[j+k]/Cum[j]
                #print(Cum[j+k],Cum[j],tmp)
                if tmp>0:
                    return k
        return 0
                

