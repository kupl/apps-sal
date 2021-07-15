class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        setA = set(A)
        
        prev = set()
        
        prev.add(A[0])
        
        for val in A[1:]:
            temp = set()
            
            for p in prev:
                temp.add(p|val)
                setA.add(p|val)
            prev = temp
            prev.add(val)
        return len(setA)
