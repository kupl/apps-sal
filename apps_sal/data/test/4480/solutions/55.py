class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        tot = 0
        bi = sum(A)//3
        count = 0
        
        for i in range(len(A) - 1):
            tot += A[i]
            if tot == bi:
                tot = 0
                count += 1
                
                if count == 2:
                    return True
        return False
