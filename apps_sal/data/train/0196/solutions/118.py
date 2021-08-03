class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        res = A[0]
        cur = A[0]

        for num in A[1:]:
            cur = num + max(0, cur)
            res = max(cur, res)

        presum = []
        accu = 0
        for num in A:
            accu += num
            presum.append(accu)

        postsum = [0 for i in range(len(A))]
        postsum[-1] = A[-1]
        accu = A[-1]
        curmax = A[-1]
        for i in range(len(A) - 2, -1, -1):
            accu += A[i]
            curmax = max(curmax, accu)
            postsum[i] = curmax

        for i in range(0, len(A) - 2):
            res = max(presum[i] + postsum[i + 2], res)

        return res
