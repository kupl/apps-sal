class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total = sum(A)
        if total % 3 != 0:
            return False
        i = 0
        count = A[i]
        while (i < len(A)-1) and (count != total/3):
            i += 1
            count += A[i]
            
            
        if (count != total/3) or (i+1 > len(A)-2):
            return False
        
        j = i +1
        count = A[j]
        while (j < len(A)-1) and (count != total/3):
            j += 1
            count += A[j]
           
            
        if (count != total/3) or (j+1 == len(A)):
            return False
        
        if sum(A[j+1:]) == total/3:
            return True
        else:
            return False
        
        
            

