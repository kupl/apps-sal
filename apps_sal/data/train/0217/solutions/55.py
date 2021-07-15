class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        sets=[{i} for i in A]
        for i in range(1,len(A)):
            for prev in sets[i-1]:
                sets[i].add(A[i]|prev)
        
        for num in sets[1:]:
            sets[0]|=num  
        return len(sets[0])
