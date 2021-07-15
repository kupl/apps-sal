
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        
        total = sum(A)
        curr_sum = 0
        first_found_flag = False
        
        for i in range(len(A) - 1): #will go until the last element.
            curr_sum += A[i]
            if not first_found_flag: #looking for the first group
                if curr_sum == total / 3: #we found the first group.
                    first_found_flag = True
            else: #looking for the second group
                if curr_sum == total * 2 / 3:
                    return True
                
        return False
            
        

