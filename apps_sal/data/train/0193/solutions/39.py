class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        length=len(arr)
        bar=length//2
        d={}
        for i in range(len(arr)):
            d[arr[i]]=d.get(arr[i],0)+1
        res=0
        l=list(sorted(d.values(),reverse=True))
        for value in l:
            length-=value
            res+=1
            if length<=bar:
                return res
        return res
