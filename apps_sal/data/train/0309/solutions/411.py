class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        # 这题bottom up写起来快?
        dp = defaultdict(lambda: 1)  # default 是 1， 自己肯定是自己的seq
        for i in range(len(A)):
            for j in range(i):  # 之前的
                diff = A[i] - A[j]
                dp[(i, diff)] = 1 + dp[(j, diff)]  # 加速 这里不需要用max来取因为是从前往后遍历，最后valid的diff肯定是最大的

        return max(dp.values())
