class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total = sum(A)
        if total % 3 != 0:
            return False
        
        subtotal = total // 3
        
        pre_sum = 0
        k = 3
        for i in range(len(A)):
            pre_sum += A[i]
            if k > 1 and pre_sum == subtotal:
                k -= 1
                pre_sum = 0
            elif i == len(A)-1:
                k -= 1
        
        return k == 0 and pre_sum == subtotal
        
        
        

