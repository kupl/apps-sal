class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        fullSet = set()
        setAtI = {0}
        
        for i in range(len(A)):
            setAtI = {A[i]| y for y in setAtI} | {A[i]}
            fullSet |=setAtI
        return len(fullSet)
        
        

