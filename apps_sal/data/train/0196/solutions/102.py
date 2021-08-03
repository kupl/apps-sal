class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        negateA = [-x for x in A]
        print(negateA)
        cursum = 0
        res = float('-inf')
        for v in negateA:
            cursum = max(v, cursum + v)
            res = max(res, cursum)

        print(res)
        res1 = float('-inf')
        cursum = 0
        for v in A:
            cursum = max(v, cursum + v)
            res1 = max(res1, cursum)
        print(res1)
        return max(res1, sum(A) + (res)) if res1 > 0 else res1
#         min maxsum
#         0,6

        # total, maxSum, curMax, minSum, curMin = 0, A[0], 0, A[0], 0
        # for a in A:
        #     curMax = max(curMax + a, a)
        #     maxSum = max(maxSum, curMax)
        #     curMin = min(curMin + a, a)
        #     minSum = min(minSum, curMin)
        #     total += a
        # print(maxSum, total , minSum)
        # return max(maxSum, total - minSum) if maxSum > 0 else maxSum
# 1 -2 3 -2
#  [-1,2,-3,2]
# cu -1  2  -1 1
# re. -1  2  2 2

# sum-min(subARR)
# SUM+MAX()
