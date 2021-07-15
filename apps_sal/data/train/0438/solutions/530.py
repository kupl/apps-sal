class DisjointSet:
    def __init__(self, nums,p='left'):
        self.parent = {i: i for i in nums}
        self.height = {i: 0 for i in nums}
        self.count = len(nums)
        self.p=p

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)
        if xRoot == yRoot:
            return xRoot
        if self.p=='left':
            (lower, higher) = (
                xRoot, yRoot) if xRoot > yRoot else (yRoot, xRoot)
        else:
            (lower, higher) = (
                xRoot, yRoot) if xRoot < yRoot else (yRoot, xRoot)
        self.parent[lower] = higher
        if self.height[higher] == self.height[lower]:
            self.height[higher] += 1
        self.count -= 1
        return higher
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n=len(arr)
        left=DisjointSet(list(range(len(arr))),'left')
        right=DisjointSet(list(range(len(arr))),'right')
        state=[0]*(len(arr))
        count=collections.defaultdict(int)
        latest=-1
        for step,idx in enumerate(arr):
            idx-=1
            state[idx]=1
            l=r=idx
            if idx>0 and state[idx-1]>0:
                left.union(idx,idx-1)
                right.union(idx,idx-1)
                
            if idx<n-1 and state[idx+1]>0:
                right.union(idx,idx+1)
                left.union(idx,idx+1)
            l=left.find(idx)
            r=right.find(idx)
            count[idx-l]-=1
            count[r-idx]-=1
            count[r-l+1]+=1
            if count[m]>=1:
                latest=step+1
            # print(idx,state,count,left.parent,right.parent,l,r)
        return latest

