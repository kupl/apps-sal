class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n=len(arr)
        lens=[0]*(n+2)
        count=[0]*(n+2)
        res=-1
        for i,num in enumerate(arr):
            if lens[num]:
                continue
            l=lens[num-1]
            r=lens[num+1]
            t=l+r+1
            lens[num-l]=lens[num+r]=lens[num]=t
            count[l]-=1
            count[r]-=1
            count[t]+=1
            if count[m]:
                res=i+1
        return res
