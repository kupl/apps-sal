class Solution:
    def numOfSubarrays(self, A, k, target):     
        # NOTE:
        #     - Since avg = sum/k , and \"k\" is fixed, we can work with the (minimum) \"sum\" directly 
        #     - So we can multiple \"target\" by \"k\"
        target *= k
        #
        # s: temporary \"sum\" for the latest sub-array of size k
        s = 0
        for i in range(k):
            s += A[i]
        # res: Final result counter
        res     = 1 if s>=target else 0
        #
        for i in range( len(A) - k ):
            s   += - A[i] + A[i+k]
            res += 1 if s>=target else 0
        return res
