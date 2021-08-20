class Solution:

    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        ans = [0]
        for (r, n) in enumerate(A):
            (maxVal, curVal) = (0, 0)
            for l in range(max(0, r - K + 1), r + 1)[::-1]:
                if A[l] > maxVal:
                    maxVal = A[l]
                if ans[l] + (r - l + 1) * maxVal > curVal:
                    curVal = ans[l] + (r - l + 1) * maxVal
            ans.append(curVal)
        return ans[-1]
