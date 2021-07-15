class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        if sum(A)%3 != 0:
            return False
        
        count, tmp_sum, target = 0, 0, sum(A)//3
        
        for num in A:
            tmp_sum += num
            if tmp_sum == target:
                count += 1 
                tmp_sum = 0
        
        return count >= 3
