class Solution:
    import math
    from itertools import permutations
    def reorderedPowerOf2(self, N: int) -> bool:
        k=str(N)
        a=[x for x in k]
        n=len(k)
        print(a,n)
        ans=list(permutations(k))
        m=0
        #print(ans)
        for i in ans:
            s=''.join(i)
            
            if s[0]!='0' :
                z=math.log(int(s),2)
                if abs(z-int(z))<0.000000001:
                    return True
        
        return False
