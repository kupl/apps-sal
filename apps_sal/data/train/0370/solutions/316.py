import math
class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        n = max(A)
        array = [0] * (n+1)
        for i in range(n+1):
            array[i] = i
        
        def find(x:int) ->int:
            if x != array[x]:
                array[x] = find(array[x])
            return array[x]
            
        def union(x:int, y:int):
            xp = find(x)
            yp = find(y)
            if xp != yp:
                array[yp] = xp
        
        length = len(A)
        for i in range(length):
            for j in range(2, int(math.sqrt(A[i]))+1):
                if A[i]%j == 0:
                    union(j,A[i])
                    union(A[i],A[i]//j)
        maximum = 0
        res = {}
        for i in range(length):
            pal = find(A[i])
            maximum = max(maximum,res.get(pal,0)+1)
            res[pal] = res.get(pal,0) + 1
        return maximum

