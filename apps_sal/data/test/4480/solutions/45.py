class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total = sum(A)
        if total % 3 != 0:
            return False
        
        partition_sum = total/3
        numberofpartition=0
        tempsum=0
        for i in range(len(A)):
            tempsum+=A[i]
            if tempsum == partition_sum:
                numberofpartition+=1
                tempsum=0
            
            if numberofpartition == 3:
                return True
        return False
