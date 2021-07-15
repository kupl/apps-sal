class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        h={}
        for e in arr:
            if e in h:
                h[e] +=1
            else:
                h[e] =1
        l=list(h.values())
        l.sort()
        while k>0:
            k= k-l[0]
            if k>=0:
                l.pop(0)
        return len(l)                

