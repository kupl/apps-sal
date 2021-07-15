class Solution:
    def findLengthOfShortestSubarray(self, A):
        # For each i, let's look at the best answer A[..i] + A[j..]
        # This requires:
        #   A[..i] monotone increasing;  (1)
        #   A[j..] monotone increasing;  (2)
        #   A[i] <= A[j]                 (3)
        
        # For each i, lets say the lowest (ie. best) such j = opt(i).
        # It turns out that opt(i) is monotone increasing, so we can use
        # two pointers.
        
        N = len(A)
        j = N - 1
        while j and A[j - 1] <= A[j]:
            j -= 1
        
        ans = j
        # j is lowest such that A[j..] is monotone increasing
        for i in range(j):
            if i and A[i-1] > A[i]:
                break
            while j < N and A[i] > A[j]:
                j += 1
            # Now, j = opt(i): ie., the lowest j such that
            # all 3 conditions (1), (2), (3) above are satisified.
            ans = min(ans, j - i - 1)
        
        return ans
