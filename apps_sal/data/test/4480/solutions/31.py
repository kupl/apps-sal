class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        target = sum(A)//3
        
        temp = 0
        count = 0
        for i in range(len(A)):
            temp += A[i]
            if(temp == target):
                temp = 0
                count += 1
                if(count == 3):
                    return True
        return False
                
        

