class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        tot = 0
        mn, mx = float('inf'), float('-inf')
        curmx, curmn = 0, 0
        for num in A:
            curmn = min(curmn + num, num)
            mn = min(mn, curmn)
            curmx = max(curmx + num, num)
            mx = max(mx, curmx)
            tot += num

        if tot == mn:
            return mx
        return max(mx, tot - mn)
