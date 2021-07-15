class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        count = Counter(A)
        for x in sorted(A, key = abs):
            if count[x]==0: continue # x may be end of a pair
            if count[2*x]==0: 
                return False # x exsist, we have to match it with a 2x
            count[2*x] -= 1
            count[x] -= 1
        return True
