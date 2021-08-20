class Solution:

    def longestSubarray(self, A):
        if not A:
            return 0
        n = len(A)
        right = 0
        cnt = 0
        res = 0
        for left in range(n):
            while right <= n - 1 and (cnt == 0 or A[right] == 1):
                cnt += A[right] == 0
                right += 1
            res = max(res, right - left)
            cnt -= A[left] == 0
        return res - 1
