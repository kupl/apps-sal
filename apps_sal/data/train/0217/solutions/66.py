class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        vals = set()
    
        if len(A) < 2:
            return len(A)
        
        cur = {0}
        for a in A:
            cur = {a| y for y in cur} | {a}
            vals |= cur
        return len(vals)
