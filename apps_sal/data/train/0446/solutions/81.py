from collections import defaultdict
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        di=defaultdict(int)
        for i in arr:di[i]+=1
        p=sorted(list(di.items()),key=lambda x:x[1])
        n=len(p)
        i=0
        while(k>0):
            if k-p[i][1]>=0:
                n-=1
            k-=p[i][1]
            i+=1
        return n
            
            

