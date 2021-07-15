
class Subset:
    
    def __init__(self,parent,rank):
        self.parent=parent
        self.rank=rank
        
def find(subsets,node):
    if subsets[node].parent!=node:
        subsets[node].parent=find(subsets,subsets[node].parent)
    return subsets[node].parent

def union(subsets,x,y):
    
    xr=find(subsets,x)
    yr=find(subsets,y)
    if xr==yr:
        return True
    else:
        xr=subsets[xr]
        yr=subsets[yr]
        
        if xr.rank<yr.rank:
            xr.parent=yr.parent
            yr.rank+=xr.rank
        elif xr.rank>yr.rank:
            yr.parent=xr.parent
            xr.rank+=yr.rank
        else:
            xr.parent=yr.parent
            yr.rank=2*yr.rank
            
        return False
    
class Solution:
    
    def findLatestStep(self, arr: List[int], m: int) -> int:
        
        
        
        a=[0 for ii in range(len(arr))]
        subsets=[Subset(i,1) for i in range(len(arr))]
        groups=set()
        ans=-1
        for j in range(len(arr)):
            i=arr[j]-1
            p=find(subsets,i)
            a[i]=1
            if i-1>=0 and a[i-1]==1:
                if find(subsets,i-1) in groups:
                   groups.remove(find(subsets,i-1))
                union(subsets,i-1,i)
            if i+1<=len(arr)-1 and a[i+1]==1:
                if find(subsets,i+1) in groups:
                    groups.remove(find(subsets,i+1))
                union(subsets,i+1,i)
            if subsets[find(subsets,i)].rank==m:
                groups.add(find(subsets,i))
            if subsets[find(subsets,i)].rank!=m and find(subsets,i) in groups:
                groups.remove(find(subsets,i))
            if len(groups):
                ans=j+1
            
        return ans
            
            

