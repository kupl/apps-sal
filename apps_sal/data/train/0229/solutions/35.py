from collections import Counter
    

class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        if not A: return True
        c = Counter(A)
        keys = sorted(c.keys())
        for k in keys:
            if k == 0:
                if c[k] % 2 == 0:
                    c[k] = 0
                else:
                    return False
            if k < 0 and c[k] > 0:
                if k/2 in c:
                    c[k/2] -= c[k]
                    c[k] = 0
            if k > 0 and c[k] > 0:
                if k*2 in c:
                    c[k*2] -= c[k]
                    c[k] = 0
            
        return set(c.values()) == {0}

