class Solution:

    def numOfSubarrays(self, A, k, target):
        target *= k
        s = 0
        for i in range(k):
            s += A[i]
        res = 1 if s >= target else 0
        for i in range(len(A) - k):
            s += -A[i] + A[i + k]
            res += 1 if s >= target else 0
        return res
