class Solution:
    def numSubarraysWithSum(self, A, S):
        return self.numSubarraysAtMostSum(A, S) - self.numSubarraysAtMostSum(A, S - 1)
    
    def numSubarraysAtMostSum(self, A, S):
        if S < 0:
            return 0
        if not A:
            return 0
        n = len(A)
        right = 0
        now_sum = 0
        res = 0
        for left in range(n):
            while right <= n - 1 and (now_sum < S or A[right] == 0):
                now_sum += A[right]
                right += 1
            res += right - left
            now_sum -= A[left]
        return res                             
