class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        h = {0: 1}
        count = summ = 0
        
        for i in range(0, len(A)):
            summ += A[i]
            if summ - S in h:
                count += h[summ-S]
            if summ not in h:
                h[summ] = 0
            h[summ]+=1
        
        return count
