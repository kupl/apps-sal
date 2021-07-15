from collections import defaultdict
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        # adj=defaultdict(set)
        po = dict()
        for i in range(lo,hi+1):
            po[i]=0
            curr=i
            while curr!=1:
                if curr&1:
                    child=curr*3+1
                else:
                    child=curr//2
                # adj[curr].add(child)
                curr=child
                po[i]+=1
            
        
        res=sorted(po.items(),key = lambda x : x[1])
        return res[k-1][0]
