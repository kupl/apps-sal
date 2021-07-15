class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        if A == None or len(A) == 0 or K == None:
            return 0
        if len(A) <= K:
            return K
        
        left = 0
        count_of_zero = 0
        maxlength = 0
        for i, num in enumerate(A):
            if A[i] == 0:
                count_of_zero += 1
            if count_of_zero <= K:
                maxlength = max(maxlength, i - left + 1)
                
            while left < i and count_of_zero > K:
                if A[left] == 0:
                    count_of_zero -=1
                left += 1

        return maxlength
            
            
        

