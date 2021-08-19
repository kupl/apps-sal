class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        res = []
        preSum = [0] * (n + 1)
        for i in range(n):
            preSum[i + 1] = preSum[i] + nums[i]

        for i in range(n):
            for j in range(i, n):
                res.append(preSum[j + 1] - preSum[i])
        res.sort()
        Sum = 0
        # print(res)
        for i in range(left, right + 1):
            Sum += res[i - 1]
        return Sum % (10**9 + 7)
