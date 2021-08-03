class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:

        ans = 0
        lo = 0
        hi = 0

        d = collections.defaultdict(int)
        while(hi < len(A)):
            d[A[hi]] += 1

            while d[0] > K:
                d[A[lo]] -= 1
                if d[A[lo]] == 0:
                    del d[A[lo]]
                lo += 1
            ans = max(ans, hi - lo + 1)
            hi += 1
        return ans
