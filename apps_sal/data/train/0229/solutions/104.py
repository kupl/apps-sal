from collections import Counter
class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        a = sorted(A,key=lambda x:abs(x),reverse = True)
        b = dict(Counter(A))
        while a:
            
            aa = a.pop()
            if aa in b:

                b[aa] -= 1
                if b[aa]==0:
                    del b[aa]

                if 2*aa in b:
                    b[2*aa] -= 1
                else:
                    return False
                if b[2*aa]==0:
                    del b[2*aa]
        return True

