from math import inf as oo


class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        total = sum(arr)
        kadanes = self.maxSubArraySum(arr)
        if (k < 2):
            return kadanes % (10**9 + 7)
        if (total > 0):
            return (kadanes + (k - 1) * total) % (10**9 + 7)
        stitchedKadanes = self.maxSubArraySum(arr * 2)
        return stitchedKadanes % (10**9 + 7)

    def maxSubArraySum(self, a):
        size = len(a)
        max_so_far = -oo
        max_ending_here = 0

        for i in a:
            max_ending_here += i
            if max_ending_here < 0:
                max_ending_here = 0
            max_so_far = max(max_so_far, max_ending_here)

        return max_so_far
