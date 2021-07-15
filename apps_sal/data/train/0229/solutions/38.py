class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        A.sort()
        B = OrderedDict()
        for x in A:
            if x in B:
                B[x] += 1
            else:
                B[x] = 1
        
        while B:
            x = next(iter(B))
            freq = B.pop(x)
            
            #print(x,freq)
            
            if x<0:
                if x%2:
                    return False
                if (x//2 not in B) or B[x//2]<freq:
                    return False
                B[x//2] -= freq
                if B[x//2] == 0:
                    B.pop(x//2)
            
            elif x==0:
                if freq%2:
                    return False
                
            else:
                if (x*2 not in B) or B[x*2]<freq:
                    return False
                B[x*2] -= freq
                if B[x*2] == 0:
                    B.pop(x*2)
        
        return True

