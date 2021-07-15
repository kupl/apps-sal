class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        n=len(arr)
        if n%2:
            return 0
        d=defaultdict(int)
        for a in arr:
            d[a%k]+=1
        if k%2==0 and k//2 in d:
            if d[k//2]%2:
                return 0
            del d[k//2]
    
        sd=sorted(d.items(),key=lambda x:x[0])
        if sd[0][0]==0:
            if sd[0][1]%2:
                return 0
            sd.pop(0)
        if n%2 and len(sd)%2:
            return 0
        while sd:
            a1=sd.pop(0)
            s2=sd.pop(-1)
            if a1[0]+s2[0]!=k or a1[1]!=s2[1]:
                return 0 
        return 1
