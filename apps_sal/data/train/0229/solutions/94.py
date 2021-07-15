class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        A_sorted = sorted(A, key=abs)
        count = collections.Counter(A)
        for a in A_sorted:
            if count[a] == 0: 
                continue
            if count[a * 2] == 0:
                return False
            count[a] -= 1
            count[a * 2] -= 1
            
        return True
