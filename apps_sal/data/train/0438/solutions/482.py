class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        res,matchGroups=-1,set()
        uf={}
        groupSize=defaultdict(lambda: 1)
        def find(x):
            uf.setdefault(x,x)
            if uf[x]!=x:
                uf[x]=find(uf[x])
            return uf[x]
        def union(x,y):
            nonlocal groupId
            gx,gy=find(x),find(y)
            if gx==gy:
                return
            if gx in matchGroups:
                matchGroups.remove(gx)
            if gy in matchGroups:
                matchGroups.remove(gy)
            size=groupSize[find(x)]+groupSize[find(y)]
            uf[find(x)]=find(y)
            groupSize[find(x)]=size
        cur=[0]*(len(arr)+2)
        for i,num in enumerate(arr):
            cur[num]=1
            if cur[num-1]==1:
                union(num,num-1)
            if cur[num+1]==1:
                union(num,num+1)
            groupId=find(num)
            if groupSize[find(num)]==m:
                matchGroups.add(groupId)
            if matchGroups:
                res=i+1
        return res
