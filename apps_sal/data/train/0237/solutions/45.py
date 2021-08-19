class Solution:

    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        ans = 0
        (il, ih, sl, sh) = (0, 0, 0, 0)
        for (j, x) in enumerate(A):
            sl += x
            while il < j and sl > S:
                sl -= A[il]
                il += 1
            sh += x
            while ih < j and (sh > S or (sh == S and (not A[ih]))):
                sh -= A[ih]
                ih += 1
            if sl == S:
                ans += ih - il + 1
        return ans
