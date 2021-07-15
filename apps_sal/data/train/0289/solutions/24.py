class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        # Let's try a relatively naive solution first.
        # Compute the cumsums. Let cumsum(k) be the cumsum upto and incl. A[k]
        # Now, V(i,j) = cumsum(i+L-1) - cumsum(i-1) + cumsum(j+M-1) - cumsum(j-1)
        # With i and j satisfying the constraints.
        # Then we simply have to maximize this value over all possible values of i and j
        # subject to the constraint.
        
        n = len(A)
        # Corner cases
        if L + M == n:
            return sum(A)
        
        # We'll use array with cumsum[k] equivalent to cumsum(k-1) being the cumsum of the first
        # k elements (i.e. upto and including A[k-1]). A[0] = 0, being the cumsum of the first zero elements.
        cumsum = [0]*(n+1)
        for i in range(n):
            cumsum[i+1] = cumsum[i] + A[i]
            
        def good_combo(i, j):
            # Return True <=> L-length subarray at i intersects with M-length subarry starting at j
            return i+L-1 < j or j+M-1 < i
            
        res = -float('inf')
        for i in range(n-L+1):
            for j in range(n-M+1):
                if good_combo(i, j):
                    res = max(res, cumsum[i+L] - cumsum[i] + cumsum[j+M] - cumsum[j])
        return res
                

