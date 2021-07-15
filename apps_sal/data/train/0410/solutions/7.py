class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        def helper(x):
            steps=0
            while x!=1:
                if x&1:
                    x=x*3+1
                else: x//=2
                steps+=1
            return steps
        
        lookup={}
        for x in range(lo,hi+1):
            lookup[x]=helper(x)
        return sorted(lookup.items(),key=lambda x:x[1])[k-1][0]
