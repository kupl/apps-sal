class Solution:

    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        dp_sum = [0 for _ in range(len(A) + 1)]
        for i in range(len(A)):
            seg_max = A[i]
            for j in range(1, K + 1):
                if i - j + 1 < 0:
                    break
                seg_max = max(seg_max, A[i - j + 1])
                tmp = dp_sum[i - j + 1] + seg_max * j
                dp_sum[i + 1] = max(dp_sum[i + 1], tmp)
        return dp_sum[-1]
