class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d={}
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        d=sorted(list(d.items()),key=lambda x:-x[1])
        d=[list(i) for i in d]
        for k0 in range(k):
            d[-1][1]-=1
            if d[-1][1]==0:
                d.pop()
        return len(d)

