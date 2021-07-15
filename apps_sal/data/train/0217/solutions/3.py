class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        prev = set()
        curr = set()
        vals = set(A)
        
        for x in A:
            curr.add(x)
            for y in prev:
                curr.add(x|y)
                vals.add(x|y)
            prev = curr
            curr = set()
        
        return len(vals)

